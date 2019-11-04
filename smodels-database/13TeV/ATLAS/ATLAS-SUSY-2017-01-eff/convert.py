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
info 				= MetaInfoInput('ATLAS-SUSY-2017-01')
info.url 			= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2017-01/'
info.sqrts 			= 13
info.lumi 			= 36.1
info.prettyName 	= 'MET'
info.private 		= False
info.arxiv 			= 'arXiv:1812.09432'
info.contact 		= 'ATLAS collaboration'
info.publication 	= 'Phys. Rev. D 100, 012006 (2019)'


SR   = {'obsN' 	: [7, 1, 5, 7, 6], 
		'expN'  : [8, 2.5, 4.6, 2.8, 5.7], 
		'bgErr' : [4, 1.3, 1.2, 1, 2.3], 
		'SR' 	: ['SRHad-Low', 'SRHad-High', 'SR1Lbb-High', 'SR1Lbb-Medium', 'SR1Lbb-Low']}

DATA = {'expExcl' : ['orig/Expectedlimit0lbb.csv', 'orig/Expectedlimit0lbb.csv', 'orig/Expectedlimit1lbb.csv', 'orig/Expectedlimit1lbb.csv', 'orig/Expectedlimit1lbb.csv'],
		'obsExcl' : ['orig/Observedlimit0lbb.csv', 'orig/Observedlimit0lbb.csv', 'orig/Observedlimit1lbb.csv', 'orig/Observedlimit1lbb.csv', 'orig/Observedlimit1lbb.csv'], 
		'effMap'  : ['orig/EffMap_TChiWH_SRHad-Low.txt', 'orig/EffMap_TChiWH_SRHad-High.txt', 'orig/EffMap_TChiWH_SR1Lbb-High.txt', 'orig/EffMap_TChiWH_SR1Lbb-Medium.txt', 'orig/EffMap_TChiWH_SR1Lbb-Low.txt'],
		'fig'	  : ['12a.png', '12a.png', '12b.png', '12b.png', '12b.png']}

for i in range(len(SR['obsN'])):
	#+++++++ dataset block ++++++++++++++
	dataset = DataSetInput(SR['SR'][i])
	dataset.setInfo(dataType = 'efficiencyMap', dataId = SR['SR'][i], observedN = SR['obsN'][i], expectedBG = SR['expN'][i], bgError = SR['bgErr'][i])
	#+++++++ next txName block ++++++++++++++
	newTx 							= dataset.addTxName('TChiWH')
	newTx.checked 					= 'No'
	newTx.constraint 				= "[[['W']],[['higgs']]]"
	newTx.conditionDescription 		= None
	newTx.condition 				= None
	newTx.source 					= 'ATLAS'
	#+++++++ next mass plane block ++++++++++++++
	newPlane 						= newTx.addMassPlane(2*[[x, y]])
	newPlane.figure 				= 'Fig.12a'
	newPlane.figureUrl 				= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2017-01/fig_' + DATA['fig'][i]
	newPlane.dataUrl 				= 'https://www.hepdata.net/record/ins1711261?version=1&table=Upper limit 0lbb'
	newPlane.setSources(dataLabels 	= ['expExclusion', 'obsExclusion', 'efficiencyMap'],
					dataFiles 		= [DATA['expExcl'][i], DATA['obsExcl'][i], DATA['effMap'][i]],
					dataFormats		= ['csv', 'csv', 'txt'])

databaseCreator.create()
