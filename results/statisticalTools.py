#!/usr/bin/env python3

""".. module:: statisticalTools.
        :synopsis: Functions for computing statistical tests and likelihoods

.. moduleauthor:: Andre Lessa
"""

from scipy import stats, optimize
import numpy as np


def getToyResults(nExpected,nError,nToys=10000):
    """
    Generates a distribution of toy results for a given value
    of expected events and its error. Assumes a gaussian distribution for
    the error (nuisance parameter).
    The procedure generates the statistical distribution of events considering
    all possible values for the expected number of events.
    It should be equivalent to the marginalized lileklihood.
    
    :param nExpected: number of expected events 
    :param nError: error for the number of expected events
    :param nToys: number of toy experiments to be generated
    
    :return: A numpy array with the number of events for each toy experiment
    """
    
    #First select an expected number of events using a gaussian distribution:
    expectedValues = stats.norm.rvs(loc=nExpected, scale=nError,
                                        size=nToys)
    
    #Remove negative values for number of expected events:
    expectedValues = expectedValues[expectedValues >= 0]
    
    # For each toy experiment, get the actual number of events by
    # taking one value from a Poisson distribution created using the expected
    # number of events previously selected.
    toyEvents = np.array(list(map(stats.poisson.rvs, expectedValues)))
    
    return toyEvents    


@np.vectorize
def likelihood(nobs,nExpected,nError,theta=0):
    """
    Likelihood value for a given number of observed events, expected events, the
    error on the number of expected events and a given value of the nuisance parameter theta.

    :param nobs: number of observed events
    :param nExpected: number of expected events 
    :param nError: error for the number of expected events
    :param theta: value for the nuisance parameter
    
    :return: The likelihood value.
    """ 
    
    lmbda = nExpected + theta
    poisson = stats.poisson.pmf(int(nobs), lmbda)
    gaussian = stats.multivariate_normal.pdf(theta,mean=0.,cov=nError**2)
    
    return gaussian*poisson

@np.vectorize
def profileLikelihood(nobs,nExpected,nError,disp=False):
    """
    The profiled likelihood value for a given number of observed events, expected events and
    its error. The value of the nuisance parameter is chosen so the likelihood value is maximized.

    :param nobs: number of observed events
    :param nExpected: number of expected events 
    :param nError: error for the number of expected events
    
    :return: profiled likelihood value.    
    """
    
    f = lambda x: -likelihood(nobs,nExpected,nError,x)
    
    theta_guess = nobs-nExpected
    
    res = optimize.fmin(f, theta_guess,full_output=True,disp=disp)
    lmax = res[1]
#     theta_max = res[0]
           
    return -lmax


@np.vectorize
def hTest(nobs,nbg,nsig,bgError,sigError,disp=False):
    """
    Computes the q value (-2*log(likelihood_ratio)) used for
    a hypothesis statistical test.
    
    :param nobs: number of observed events
    :param nbg: number of expected BG events 
    :param nsig: number of expected signal events
    :param bgError: error for the number of expected BG events
    :param sigError: error for the number of expected signal events
    
    :return: q value.
    """
    
    nExpected = nbg+nsig
    nError = np.sqrt(bgError**2+sigError**2)
    lmax = profileLikelihood(nobs,nExpected,nError,disp)
       
    #Assuming a free signal, which maximizes the likelihood (nsig = nobs-nbg)
    nExpected = nobs
    lm = profileLikelihood(nobs,nExpected,nError)
    
    if not lmax or not lm:
        return None
    
    ratio = lmax/lm
    q = -2*np.log(ratio)
    
    return q

def getCL(nobs,nExpected,nError,method='toys',nToys=5000):
    """
    Computes the CL value for a given number of observed events, expected events
    and its error.
    Two methods are available: one using the profiled likelihood ('profile') and one
    using toy experiments ('toys'), which corresponds to the marginalized likelihood.
    For the latter, the number of experiments should also be defined.
    
    :param nobs: number of observed events
    :param nExpected: number of expected events 
    :param nError: error for the number of expected events
    :param method: which method to use (profile or toys)
    :param nToys: number of toy experiments 
                  (used if method = 'toys' and for estimating the relevant range of events 
                  for which the likelihood is non-zero)
    
    :return: Probability of getting an event with value less or equal than nobs
    """    
    
    
    if method == 'profile':
        #First use a number of toy experiments to estimate which is
        #the relevant region of the likelihood to be summed over:
        toyN = getToyResults(nExpected,nError,10000)
        minN = toyN.min()
        maxN = max(nobs,toyN.max())
        #Evaluate likelihood in the relevant range
        nVals = np.arange(minN,maxN+1)
        likeVals = profileLikelihood(nVals,nExpected,nError)
        #Compute norm for the profiled likelihood
        norm = likeVals.sum()
        #Compute profiled likelihood for each number of events in the range  minN < n < maxN
        #and sum it to obtain the CL (CL = Prob(n <= nobs))
        CL = likeVals[nVals <= nobs].sum()/norm
    else:
        #Generate toy experiments:        
        toyN = getToyResults(nExpected,nError,nToys)
        #Count how many toy experiments have number of events <= nobs
        #and divide by the total number of toy experiments to get CL:
        CL = toyN[toyN <= nobs].size/toyN.size
    
    return CL


def CLs(nobs,nbg,nsig,bgError,sigError,method='profile',nToys=5000):
    """
    Computes the CLs value for a given number of observed events, expected BG and signal events
    and their error.
    Two methods are available: one using the profiled likelihood ('profile') and one
    using toy experiments ('toys'), which corresponds to the marginalized likelihood.
    For the latter, the number of experiments should also be defined.
    
    :param nobs: number of observed events
    :param nbg: number of expected BG events 
    :param nsig: number of expected signal events
    :param bgError: error for the number of expected BG events
    :param sigError: error for the number of expected signal events
    :param method: which method to use (profile or toys)
    
    :return: CLs value
    """    
    
    #-----CLb calculation (BG-only hypothesis)-----
    nExpected = nbg
    nError = bgError
    CLb = getCL(nobs,nExpected,nError,method,nToys)

    if not CLb:
        return None
        
    #-----CLsb calculation (BG+Signal hypothesis)-----
    nExpected = nbg+nsig
    nError = np.sqrt(bgError**2 + sigError**2)
    CLsb = getCL(nobs,nExpected,nError,method,nToys)
    
    return CLsb/CLb

    
