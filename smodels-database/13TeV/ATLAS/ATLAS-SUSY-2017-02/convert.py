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
info 				= MetaInfoInput('ATLAS-SUSY-2017-02')
info.url 			= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2017-02/'
info.sqrts 			= 13
info.lumi 			= 36.1
info.prettyName 	= '0L + jets + Etmiss'
info.private 		= False
info.arxiv 			= 'https://arxiv.org/abs/1806.04030'
info.contact 		= 'ATLAS collaboration'
info.publication 	= 'Phys. Rev. D 98, 092002 (2018)'

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

lsp_masses = [0., 1.]

#+++++++ next txName block ++++++++++++++
TChiH 						= dataset.addTxName('TChiH')
TChiH.checked 				= 'No'
TChiH.constraint 			= "[[['Z']],[['Z']]]+[[['higgs']],[['higgs']]]"
TChiH.conditionDescription = None
TChiH.condition 			= None
TChiH.source 				= "ATLAS"
#+++++++ next mass plane block ++++++++++++++
for lsp in lsp_masses:
	plane 						= TChiH.addMassPlane(2*[[x, lsp]])	#2*[[x, 1.]])#[[x],[x]])#2*[[x]]
	plane.figure 				= 'Fig.2'
	plane.figureUrl 			= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2017-02/figaux_02.png'
	plane.dataUrl 				= 'https://www.hepdata.net/record/ins1677389?version=1&table=Table5'
	plane.setSources(dataLabels = ['upperLimits'],
					units 		= ['fb'],
					dataFiles 	= ['orig/HEPData-ins1677389-v1-Table_6_addedG.csv'],
          			coordinates = [ { x: 0, "value": 2 } ],
					dataFormats	= ['csv'])

#plane.setSources(dataLabels = ['expExclusion', 'obsExclusion', 'upperLimits'],
#				units 		= [None, None, 'fb'],
#				dataFiles 	= ['orig/HEPData-ins1677389-v1-Table_3_exp.csv', 'orig/HEPData-ins1677389-v1-Table_3_obs.csv', 'orig/HEPData-ins1677389-v1-Table_6_addedG.csv'],
#				dataFormats	= ['csv', 'csv', 'csv'])

databaseCreator.create()
