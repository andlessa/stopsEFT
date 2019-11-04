#!/usr/bin/env python3

"""
.. module:: testInclusiveObjects
   :synopsis: Tests implementation of inclusive objects for entries in the database.

.. moduleauthor:: Andre Lessa <lessa.a.p@gmail.com>

"""
import sys
sys.path.insert(0,"../")
import unittest
from smodels.experiment.txnameObj import TxName
from smodels.tools.physicsUnits import GeV
from smodels.theory import branch,element
from smodels.experiment import infoObj
from smodels.tools.inclusiveObjects import InclusiveValue, InclusiveList


class InclusiveObjectsTest(unittest.TestCase):
    
    def testInclusiveValue(self):

        x,y = 5,10.
        z = InclusiveValue()
        self.assertTrue(x == z)
        self.assertFalse(y == z)
        self.assertTrue(str(z) == '*')

    def testInclusiveList(self):
         
        x = [1,'a',10.,-5]
        y = 'string'
        z = InclusiveList()
         
        self.assertTrue(x == z)
        self.assertFalse(y == z)
        self.assertTrue(str(z) == '[*]')
 
    def testInclusiveBranch(self):
         
        x = branch.Branch(info='[[e+],[e-,mu+]]',finalState = 'MET')
        z = branch.InclusiveBranch()
         
        self.assertTrue(x == z)
        self.assertTrue(str(z) == '[*]')
         
    def testInclusiveElement(self):
         
        el1 = element.Element(info='[[[e+],[e-,mu+]],[[*],[e-,mu+]]]',finalState = ['MET','HSCP'])
        el2 = element.Element(info='[[[e+],[e-,mu+]],[[jet],[e-,mu+]]]',finalState = ['anyOdd','HSCP'])
        el3 = element.Element(info='[[[e+],[e-,mu+]],[[jet],[e-,mu+]]]',finalState = ['HSCP','HSCP'])
        el4 = element.Element(info='[[*],[[jet],[e-,mu+]]]',finalState = ['MET','HSCP'])
        el5 = element.Element(info='[[[e+],[e-,mu+]],[[jet],[e-,mu+]]]',finalState = ['MET','HSCP'])
        el6 = element.Element(info='[[*],[*]]',finalState = ['MET','HSCP'])
        el7 = element.Element(info='[[[e+],[e-,mu+]],[[jet,jet],[e-,mu+]]]',finalState = ['MET','HSCP'])        
         
         
        self.assertTrue(el1 == el2)
        self.assertTrue(el2 == el3)
        self.assertTrue(el3 != el4)
        self.assertTrue(el2 == el4)
        self.assertTrue(el1 == el4)
        self.assertTrue(el1 != el3)
        self.assertTrue(el6 == el1)
        self.assertTrue(el6 == el2)
        self.assertTrue(el5 == el1)
        self.assertTrue(el5 != el3)
        self.assertTrue(el7 != el1)
        self.assertTrue(el1 != el7)
        self.assertTrue(str(el1) == "[[[e+],[e-,mu+]],[[*],[e-,mu+]]]")
        self.assertTrue(str(el6) == "[[*],[*]]")        
 
 
    def testInclusiveTxNameData(self):
         
        f = './database/13TeV/CMS/CMS-PAS-EXO-16-036-eff/c000/THSCPM2.txt'
        gInfo = infoObj.Info('./database/13TeV/CMS/CMS-PAS-EXO-16-036-eff/globalInfo.txt')
        gInfo.addInfo('dataId','c000')
        tx = TxName(f,gInfo,gInfo)
        res = tx.txnameData.getValueFor([[100.*GeV]]*2)
        self.assertAlmostEqual(res,0.058038)
        res = tx.txnameData.getValueFor([[500.*GeV,150.*GeV,10.*GeV],[100.*GeV]])
        self.assertAlmostEqual(res,0.058038)
                 
        res = tx.txnameData.getValueFor([[125.*GeV]]*2)
        self.assertAlmostEqual(res,0.090999)
        res = tx.txnameData.getValueFor([[200.*GeV]]*2)
        self.assertEqual(res,None)
         
        f = './database/13TeV/CMS/CMS-PAS-EXO-16-036-eff/c000/THSCPM6.txt'
        gInfo = infoObj.Info('./database/13TeV/CMS/CMS-PAS-EXO-16-036-eff/globalInfo.txt')
        gInfo.addInfo('dataId','c000')
        tx = TxName(f,gInfo,gInfo)
        res = tx.txnameData.getValueFor([[279.*GeV,170.*GeV,100.*GeV]]*2)
        self.assertAlmostEqual(res,0.097172,6)
        res = tx.txnameData.getValueFor([[100.*GeV],[279.*GeV,170.*GeV,100.*GeV]])
        self.assertAlmostEqual(res,0.097172,6)
        res = tx.txnameData.getValueFor([[500*GeV,100.*GeV],[1.917E+03*GeV,1.7E+02*GeV,1E+02*GeV]])        
        self.assertAlmostEqual(res,0.00025745,6)
        
        res = tx.txnameData.getValueFor([[500*GeV,100.*GeV,10.*GeV],[1.112E+03*GeV,188*GeV,1E+02*GeV]])
        self.assertAlmostEqual(res,0.015,3)
         
    def testInclusiveTxName(self):
         
 
        f = './database/13TeV/CMS/CMS-PAS-EXO-16-036-eff/c000/THSCPM2.txt'
        gInfo = infoObj.Info('./database/13TeV/CMS/CMS-PAS-EXO-16-036-eff/globalInfo.txt')
        gInfo.addInfo('dataId','c000')
        tx = TxName(f,gInfo,gInfo)
         
        el = element.Element(info="[[],[[e+]]]",finalState = ['HSCP','MET'])
        newEl = tx.hasElementAs(el)  #newEl should be equal to el, but with opposite branch ordering
        self.assertFalse(newEl is None)
        bsmParticles = [[str(bsm) for bsm in br] for br in newEl.oddParticles]        
        self.assertTrue(bsmParticles == [['anyOdd','MET'],['HSCP']])
        

if __name__ == "__main__":
    unittest.main()
