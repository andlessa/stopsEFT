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
info = MetaInfoInput('ATLAS-SUSY-2016-24')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/'
info.sqrts = 13
info.lumi = 36.1
info.prettyName = '2+ leptons (e,mu) + jets + Etmiss'
info.private = False
info.arxiv =  'https://arxiv.org/abs/1803.02762'
info.contact = 'ATLAS collaboration'
info.publication ='Eur. Phys. J. C 78 (2018) 995'

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)


#+++++++ next txName block ++++++++++++++
TChipChimSlepSlep 						= dataset.addTxName('TChipChimSlepSlep')
TChipChimSlepSlep.checked 				= 'No'
TChipChimSlepSlep.constraint 			= "[[['nu'],['e+']],[['nu'],['e-']]]+[[['nu'],['e-']],[['nu'],['e+']]]+[[['nu'],['mu+']],[['nu'],['mu-']]]+[[['nu'],['mu-']],[['nu'],['mu+']]]"
TChipChimSlepSlep.conditionDescription 	= None
TChipChimSlepSlep.condition 			= None
TChipChimSlepSlep.source 				= 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
TChipChimSlepSlep_1 			= TChipChimSlepSlep.addMassPlane(2*[[x, 0.5*(x+y), y]])
TChipChimSlepSlep_1.figure 		= 'Fig.8a'
TChipChimSlepSlep_1.figureUrl 	= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08a.png'
TChipChimSlepSlep_1.dataUrl 	= 'https://www.hepdata.net/record/ins1658902?version=1&table=Table78'
TChipChimSlepSlep_1.setSources(dataLabels = ['expExclusion', 'obsExclusion', 'upperLimits'],
                 dataFiles = ['orig/HEPData-ins1658902-v1-Table_13.csv', 'orig/HEPData-ins1658902-v1-Table_14.csv', 'orig/HEPData-ins1658902-v1-Table_78.csv'], 
				 units = [ None, None, 'fb' ], 
				 coordinates = [ {x: 0, y: 1, 'value': None}, {x: 0, y: 1, 'value': None},  {x : 1, y: 0, 'value' :2} ],
				 dataFormats = ['csv', 'csv', 'csv'])


#+++++++ next txName block ++++++++++++++
TSlepSlep 						= dataset.addTxName('TSlepSlep')
TSlepSlep.checked 				= 'No'
TSlepSlep.constraint 			= "[[['e+']],[['e-']]]+[[['e-']],[['e+']]]+[[['mu+']],[['mu-']]]+[[['mu-']],[['mu+']]]"#"[[['l']],[['l']]]"
TSlepSlep.conditionDescription 	= None
TSlepSlep.condition 			= None
TSlepSlep.source 				= 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 			= TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlep_1.figure 		= 'Fig.8b'
TSlepSlep_1.figureUrl 	= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08b.png'
TSlepSlep_1.dataUrl 	= 'https://www.hepdata.net/record/ins1658902?version=1&table=Table79'
TSlepSlep_1.setSources(dataLabels = ['expExclusion', 'obsExclusion', 'upperLimits'],
                 dataFiles = ['orig/HEPData-ins1658902-v1-Table_15.csv', 'orig/HEPData-ins1658902-v1-Table_16.csv', 'orig/HEPData-ins1658902-v1-Table_79.csv'],
				 units = [ None, None, 'fb' ],
				 coordinates = [ {x: 0, y: 1, 'value': None}, {x: 0, y: 1, 'value': None},  {x : 1, y: 0, 'value' :2} ],
                 dataFormats = ['csv', 'csv', 'csv'])


#+++++++ next txName block ++++++++++++++
TChiChipmSlepSlep 						= dataset.addTxName('TChiChipmSlepSlep')
TChiChipmSlepSlep.checked 				= 'No'
TChiChipmSlepSlep.constraint 			= "[[['nu'],['l']],[['e+'],['e-']]]+[[['nu'],['l']],[['e-'],['e+']]]+[[['nu'],['l']],[['mu+'],['mu-']]]+[[['nu'],['l']],[['mu-'],['mu+']]]"
TChiChipmSlepSlep.conditionDescription 	= None
TChiChipmSlepSlep.condition 			= None
TChiChipmSlepSlep.source 				= 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepSlep_1 			= TChiChipmSlepSlep.addMassPlane(2*[[x, 0.5*(x+y), y]])
TChiChipmSlepSlep_1.figure 		= 'Fig.8c'
TChiChipmSlepSlep_1.figureUrl 	= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08c.png'
TChiChipmSlepSlep_1.dataUrl 	= 'https://www.hepdata.net/record/ins1658902?version=1&table=Table80'
TChiChipmSlepSlep_1.setSources(dataLabels = ['expExclusion', 'obsExclusion', 'upperLimits'],
                 dataFiles = ['orig/HEPData-ins1658902-v1-Table_17.csv', 'orig/HEPData-ins1658902-v1-Table_18.csv', 'orig/HEPData-ins1658902-v1-Table_80.csv'], 
				 units = [ None, None, 'fb' ],
				 coordinates = [ {x: 0, y: 1, 'value': None}, {x: 0, y: 1, 'value': None},  {x : 1, y: 0, 'value' :2} ],
				 dataFormats = ['csv', 'csv', 'csv'])


#+++++++ next txName block ++++++++++++++
TChiWZ 						= dataset.addTxName('TChiWZ')
TChiWZ.checked 				= 'No'
TChiWZ.constraint 			= "[[['W']],[['Z']]]"
TChiWZ.conditionDescription = None
TChiWZ.condition 			= None
TChiWZ.source 				= 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
TChiWZ_1 			= TChiWZ.addMassPlane(2*[[x, y]])
TChiWZ_1.figure 	= 'Fig.8d'
TChiWZ_1.figureUrl 	= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08d.png'
TChiWZ_1.dataUrl 	= 'https://www.hepdata.net/record/ins1658902?version=1&table=Table81'
TChiWZ_1.setSources(dataLabels = ['expExclusion', 'obsExclusion', 'upperLimits'],
                 dataFiles = ['orig/HEPData-ins1658902-v1-Table_19.csv', 'orig/HEPData-ins1658902-v1-Table_20.csv', 'orig/HEPData-ins1658902-v1-Table_81.csv'],
				 units = [ None, None, 'fb' ],
				 coordinates = [ {x: 0, y: 1, 'value': None}, {x: 0, y: 1, 'value': None},  {x : 1, y: 0, 'value' :2} ],
                 dataFormats = ['csv', 'csv', 'csv'])

databaseCreator.create()










