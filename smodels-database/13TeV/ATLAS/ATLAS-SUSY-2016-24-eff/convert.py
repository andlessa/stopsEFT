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

SF   = {'obsN' 	: [153, 9], 
		'expN'  : [133, 9.8], 
		'bgErr' : [22, 2.9], 
		'SR' 	: ['SR2-SF-loose', 'SR2-SF-tight']}
DF   = {'obsN' 	: [78, 11, 6, 2], 
		'expN'  : [68, 11.5, 2.1, 0.6], 
		'bgErr' : [7, 3.1, 1.9, 0.6], 
		'SR' 	: ['SR2-DF-100', 'SR2-DF-150', 'SR2-DF-200', 'SR2-DF-300']}
SR2  = {'obsN' 	: [11, 2, 0], 
		'expN'  : [4.2, 4.1, 1.6], 
		'bgErr' : [3.4, 2.6, 1.6], 
		'SR' 	: ['SR2-low', 'SR2-int', 'SR2-high']}
WZ   = {'obsN' 	: [21, 1, 2, 1, 3, 4], 
		'expN'  : [21.7, 2.7, 1.6, 2.2, 1.8, 1.3], 
		'bgErr' : [2.9, 0.5, 0.3, 0.5, 0.3, 0.3], 
		'SR' 	: ['WZ-0Ja', 'WZ-0Jb', 'WZ-0Jc', 'WZ-1Ja', 'WZ-1Jb', 'WZ-1Jc']}
SLEP = {'obsN' 	: [4, 3, 9, 0, 0], 
		'expN'  : [2.2, 2.8, 5.4, 1.4, 1.1], 
		'bgErr' : [0.8, 0.4, 0.9, 0.4, 0.2], 
		'SR' 	: ['slep-a', 'slep-b', 'slep-c', 'slep-d', 'slep-e']}

TChipChimSlepSlepAll = {
'name' 		 : 'TChipChimSlepSlepAll',
'info' 		 :{'figure' 		: 'Fig.8a', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08a.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table78'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_13.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_14.csv'},
#'constraint' : "0.5*([[['nu'],['L+']],[['nu'],['L-']]]+[[['nu'],['L-']],[['nu'],['L+']]])", <- DOUBLE COUNTING??
'constraint' : "[[['nu'],['L+']],[['nu'],['L-']]]",
'massPlane'  : 2*[[x, 0.5*(x+y), y]]}

TSlepSlepAll = {
'name' 		 : 'TSlepSlepAll',
'info' 		 :{'figure' 		: 'Fig.8b', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08b.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table79'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_15.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_16.csv'},
#'constraint' : "[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]",
'constraint' : "[[['L+']],[['L-']]]",
'massPlane'  : 2*[[x, y]]}

TChiChipmSlep = {
'name' 		 : 'TChiChipmSlep',
'info' 		 :{'figure' 		: 'Fig.8c', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08c.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table80'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_17.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_18.csv'},
#'constraint' : "0.5*([[['L+'],['L-']],[['L'],['nu']]] + [[['L+'],['L-']],[['nu'],['L']]] + [[['L-'],['L+']],[['L'],['nu']]] + [[['L-'],['L+']],[['nu'],['L']]])", <- NO ERROR BUT STILL DOUBLE COUNTING BY SAME LOGIC??
'constraint' : "2.0*([[['L+'],['L-']],[['L'],['nu']]] + [[['L+'],['L-']],[['nu'],['L']]])",
'massPlane'  : 2*[[x, 0.5*(x+y), y]]}

TChiWZ = {
'name' 		 : 'TChiWZ',
'info' 		 :{'figure' 		: 'Fig.8d', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08d.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table81'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_19.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_20.csv'},
'constraint' : "[[['W']],[['Z']]]",
'massPlane'  : 2*[[x, y]]}

DATA = [([TChipChimSlepSlepAll, TSlepSlepAll], SF),
		(TChipChimSlepSlepAll, DF),
		(TChiChipmSlep, SLEP),
		(TChiWZ, SR2),
		(TChiWZ, WZ),]

for TX, SR in DATA:
	for i in range(len(SR['obsN'])):
		#+++++++ dataset block ++++++++++++++
		dataset = DataSetInput(SR['SR'][i])
		dataset.setInfo(dataType = 'efficiencyMap', dataId = SR['SR'][i], observedN = SR['obsN'][i], expectedBG = SR['expN'][i], bgError = SR['bgErr'][i])
		if not isinstance(TX, list):
			#+++++++ next txName block ++++++++++++++
			newTx 							= dataset.addTxName(TX['name'])
			newTx.checked 					= 'No'
			newTx.constraint 				= TX['constraint']
			newTx.conditionDescription 		= None
			newTx.condition 				= None
			newTx.source 					= 'ATLAS'
			#+++++++ next mass plane block ++++++++++++++
			newPlane 						= newTx.addMassPlane(TX['massPlane'])
			newPlane.figure 				= TX['info']['figure']
			newPlane.figureUrl 				= TX['info']['figureUrl']
			newPlane.dataUrl 				= TX['info']['dataUrl']
			newPlane.setSources(dataLabels 	= ['expExclusion', 'obsExclusion', 'efficiencyMap'],
							dataFiles 		= [TX['sources']['expExcl'], TX['sources']['obsExcl'], 'orig/EffMap_' + TX['name'] + '_' + SR['SR'][i] + '.txt'],
							dataFormats		= ['csv', 'csv', 'txt'])
		else:
			for n in range(len(TX)):
				#+++++++ next txName block ++++++++++++++
				newTx 							= dataset.addTxName(TX[n]['name'])
				newTx.checked 					= 'No'
				newTx.constraint 				= TX[n]['constraint']
				newTx.conditionDescription 		= None
				newTx.condition 				= None
				newTx.source 					= 'ATLAS'
				#+++++++ next mass plane block ++++++++++++++
				newPlane1 						= newTx.addMassPlane(TX[n]['massPlane'])
				newPlane1.figure 				= TX[n]['info']['figure']
				newPlane1.figureUrl 			= TX[n]['info']['figureUrl']
				newPlane1.dataUrl 				= TX[n]['info']['dataUrl']
				newPlane1.setSources(dataLabels = ['expExclusion', 'obsExclusion', 'efficiencyMap'],
								dataFiles 		= [TX[n]['sources']['expExcl'], TX[n]['sources']['obsExcl'], 'orig/EffMap_' + TX[n]['name'] + '_' + SR['SR'][i] + '.txt'],
								dataFormats		= ['csv', 'csv', 'txt'])

databaseCreator.create()
