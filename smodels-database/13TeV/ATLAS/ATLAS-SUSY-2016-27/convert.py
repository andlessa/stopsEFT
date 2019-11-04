#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse

argparser = argparse.ArgumentParser(description =  
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', 
help = 'path to the package smodels_utils',\
type = str )
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
help = 'path to the package smodels_utils',\
type = str )
args = argparser.parse_args()

if args.utilsPath:
    utilsPath = args.utilsPath
else:
    databaseRoot = '../../../'
    sys.path.append(os.path.abspath(databaseRoot))
    from utilsPath import utilsPath
    utilsPath = databaseRoot + utilsPath
if args.smodelsPath:
    sys.path.append(os.path.abspath(args.smodelsPath))

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z

#+++++++ global info block ++++++++++++++
info 				= MetaInfoInput('ATLAS-SUSY-2016-27')
info.url 			= "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-27/"
info.sqrts 			= 13
info.lumi			= 36.1
info.prettyName 	= " "
info.private		= False
info.arxiv			= 'https://arxiv.org/abs/1802.03158'
info.contact		= 'ATLAS collaboration'
info.publication	= 'Phys. Rev. D 97, 092006 (2018)'

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#+++++++ next txName block ++++++++++++++
T5Gamma 						= dataset.addTxName('T5Gamma')
T5Gamma.checked 				= 'No'
T5Gamma.constraint 		 		= "[[['jet','jet'],['photon']],[['jet','jet'],['photon']]]"
T5Gamma.conditionDescription	= None
T5Gamma.condition 		 		= None
T5Gamma.source 					= "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T5Gamma_1						= T5Gamma.addMassPlane(2*[[x, y, 1.]])
T5Gamma_1.figure    			= 'Fig.8'
T5Gamma_1.figureUrl 			= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-27/fig_08.png'
T5Gamma_1.dataUrl   			= "https://www.hepdata.net/record/ins1654357?version=1&table=Cross section UL 1"
T5Gamma_1.setSources(dataLabels	= ['expExclusion', 'obsExclusion', 'upperLimits'],
				dataFiles		= ['orig/HEPData-ins1654357-v1-Exclusion_contour_(expected)_1.csv', 'orig/HEPData-ins1654357-v1-Exclusion_contour_(observed)_2.csv', 'orig/HEPData-ins1654357-v1-Cross_section_UL_1.csv'],
				units 			= [ None, None, 'fb' ],
				dataFormats 	= ['csv', 'csv', 'csv'])

#+++++++ next txName block ++++++++++++++
T6Gamma 					 	= dataset.addTxName('T6Gamma')
T6Gamma.checked 			 	= 'No'
T6Gamma.constraint 			 	= "[[['jet'],['photon']],[['jet'],['photon']]]"
T6Gamma.conditionDescription 	= None
T6Gamma.condition 			 	= None
T6Gamma.source 				 	= "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T6Gamma_1 						= T6Gamma.addMassPlane(2*[[x, y, 0.]])
T6Gamma_1.figure    			= 'Fig.9'
T6Gamma_1.figureUrl 			= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-27/fig_09.png'
T6Gamma_1.dataUrl   			= "https://www.hepdata.net/record/ins1654357?version=1&table=Cross section UL 2"
T6Gamma_1.setSources(dataLabels = ['expExclusion', 'obsExclusion', 'upperLimits'],
					dataFiles 	= ['orig/HEPData-ins1654357-v1-Exclusion_contour_(expected)_3.csv', 'orig/HEPData-ins1654357-v1-Exclusion_contour_(observed)_4.csv', 'orig/HEPData-ins1654357-v1-Cross_section_UL_2.csv'],
					units 		= [ None, None, 'fb' ],
					dataFormats = ['csv', 'csv', 'csv'])

#+++++++ next txName block ++++++++++++++
TChipChimGamma 							= dataset.addTxName('TChipChimGamma')
TChipChimGamma.checked 					= 'No'
TChipChimGamma.constraint 				= "[[['W'],['photon']],[['Z'],['photon']]]+[[['W'],['photon']],[['W'],['photon']]]+[[['W'],['photon']],[['higgs'],['photon']]]"
TChipChimGamma.conditionDescription 	= None
TChipChimGamma.condition 				= None
TChipChimGamma.source 			    	= "ATLAS"
#+++++++ next mass plane block ++++++++++++++
TChipChimGamma_1 		   				= TChipChimGamma.addMassPlane(2*[[x, y, 0.]])
TChipChimGamma_1.figure    				= 'Fig.10'
TChipChimGamma_1.figureUrl 				= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-27/fig_10.png'
TChipChimGamma_1.dataUrl   				= "https://www.hepdata.net/record/ins1654357?version=1&table=Cross section UL 3"
TChipChimGamma_1.setSources(dataLabels 	= ['expExclusion', 'obsExclusion', 'upperLimits'],
							dataFiles	= ['orig/HEPData-ins1654357-v1-Exclusion_contour_(expected)_5.csv', 'orig/HEPData-ins1654357-v1-Exclusion_contour_(observed)_6.csv', 'orig/HEPData-ins1654357-v1-Cross_section_UL_3.csv'],
							units		= [ None, None, 'fb' ],
							dataFormats	= ['csv', 'csv', 'csv'])

#+++++++ next txName block ++++++++++++++
T5ZGamma 					  		= dataset.addTxName('T5ZGamma')
T5ZGamma.checked 			  		= 'No'
T5ZGamma.constraint 		  		= "[[['jet','jet'],['Z']],[['jet','jet'],['photon']]]"
T5ZGamma.conditionDescription 		= None
T5ZGamma.condition 			  		= None
T5ZGamma.source 			  		= "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T5ZGamma_1 							= T5ZGamma.addMassPlane(2*[[x, y, 0.]])
T5ZGamma_1.figure    				= 'Fig.11'
T5ZGamma_1.figureUrl 				= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-27/fig_11.png'
T5ZGamma_1.dataUrl   				= "https://www.hepdata.net/record/ins1654357?version=1&table=Cross section UL 4"
T5ZGamma_1.setSources(dataLabels	= ['expExclusion', 'obsExclusion', 'upperLimits'],
						dataFiles	= ['orig/HEPData-ins1654357-v1-Exclusion_contour_(expected)_7.csv', 'orig/HEPData-ins1654357-v1-Exclusion_contour_(observed)_8.csv', 'orig/HEPData-ins1654357-v1-Cross_section_UL_4.csv'],
						units		= [ None, None, 'fb' ],
						dataFormats	= ['csv', 'csv', 'csv'])

databaseCreator.create()
