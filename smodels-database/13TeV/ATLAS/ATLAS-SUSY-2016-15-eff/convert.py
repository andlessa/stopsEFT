#!/usr/bin/env python3

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
info = MetaInfoInput('ATLAS-SUSY-2016-15')
info.url 		 = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-15/'
info.sqrts 		 = 13
info.lumi 		 = 36.1
info.prettyName  = 'stop to lsp'
info.private 	 = False
info.arxiv 		 = 'https://arxiv.org/abs/1709.04183'
info.contact 	 = 'ATLAS collaboration'
info.publication = 'JHEP 12 (2017) 085'

obsN 	= [11.2, 	 9.6,	  11.,	   80.,		21.7,	 19.6,	  15.1,	  11.2,	  15.3,	  3.5,	  3.2,	  6.1]
expN 	= [11.5, 	 9.6,	  8.7, 	   58.,		21.0,	 20.,	  15.8,	  13.9,	  12.3,	  6.7,	  3.0,	  6.4]
bgErr 	= [2.9, 	 2.45,	  2.0, 	   20.,		5.8,	 5.7,	  4.15,	  4.25,	  4.05,	  2.3,	  0.6,	  1.9]
SR 		= ['SRAT0', 'SRATW', 'SRATT', 'SRBT0', 'SRBTW', 'SRBTT', 'SRC1', 'SRC2', 'SRC3', 'SRC4', 'SRC5', 'SRE']
fig		= ['09c',	'09b',	 '09a',	  '09c',   '09b',	'09a',	 '10a',	 '10b',	 '10c',	 '10d',	 '10e',	 '11b']

for i in range(len(obsN)):
	#+++++++ dataset block ++++++++++++++
	dataset = DataSetInput(SR[i])
	dataset.setInfo(dataType = 'efficiencyMap', dataId = SR[i], observedN = obsN[i], expectedBG = expN[i], bgError = bgErr[i])
	#+++++++ next txName block ++++++++++++++
	T2tt 							= dataset.addTxName('T2tt')
	T2tt.checked 					= 'False'
	T2tt.constraint 				= '[[[t]],[[t]]]'
	T2tt.conditionDescription 		= None
	T2tt.condition 					= None
	T2tt.massConstraint				= [['dm >= 169.0'], ['dm >= 169.0']]
	T2tt.source 					= 'ATLAS'
	#+++++++ next txName block ++++++++++++++
	T2ttoff 						= dataset.addTxName('T2ttoff')
	T2ttoff.checked 				= 'False'
	T2ttoff.constraint 				= '[[[b, W]],[[b, W]]]'
	T2ttoff.conditionDescription 	= None
	T2ttoff.condition 				= None
	T2ttoff.massConstraint 			= [['80 <= dm < 169.0'], ['80 <= dm < 169.0']]
	T2ttoff.source 					= 'ATLAS'
	#+++++++ next mass plane block ++++++++++++++
	T2bbffff						= dataset.addTxName('T2bbffff')
	T2bbffff.checked				= 'False'
	T2bbffff.constraint				= "9/4*[[['b', 'jet','jet']],[['b', 'jet','jet']]]"
	T2bbffff.conditionDescription 	= None
	T2bbffff.condition				= None
	T2bbffff.source					= 'ATLAS'
	T2bbffff.massConstraint			= [['dm < 80'], ['dm < 80']]
	#+++++++ next mass plane block ++++++++++++++
	T2tt_1 							= T2tt.addMassPlane(2*[[x, y]])
	T2tt_1.figure 					= 'Fig.' + fig[i]
	T2tt_1.figureUrl 				= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-15/figaux_' + fig[i] + '.png'
	T2tt_1.dataUrl 					= 'https://www.hepdata.net/record/ins1623207?version=7&table=Eff' + SR[i]
	T2tt_1.setSources(dataLabels 	= ['expExclusion', 'obsExclusion', 'efficiencyMap'],
						dataFiles 	= ['orig/ExpectedexclusioncontourdirectTT.csv', 'orig/ObservedexclusioncontourdirectTT.csv', 'orig/EffMap_T2tt_' + SR[i] + '.txt'],
						coordinates = [ {x: 0, y: 1, 'value': None}, {x: 0, y: 1, 'value': None},  {x : 1, y: 0, 'value' :2} ],																	 
						dataFormats	= ['csv', 'csv', 'txt'])

	T2ttoff.addMassPlane(T2tt_1)
	T2bbffff.addMassPlane(T2tt_1)

'''

obsN 	= [17.9, 10.9]
expN 	= [16.4, 8.0]
bgErr 	= [5.15, 2.35]
SR 		= ['SRDlow', 'SRDhigh']

for i in range(len(obsN)):
	#+++++++ dataset block ++++++++++++++
	dataset = DataSetInput(SR[i])
	dataset.setInfo(dataType = 'efficiencyMap', dataId = SR[i], observedN = obsN[i], expectedBG = expN[i], bgError = bgErr[i])
	#+++++++ next txName block ++++++++++++++
	T2bb 									= dataset.addTxName('T2bb')
	T2bb.checked 							= 'False'
	T2bb.constraint 						= '[[[b]],[[b]]]'
	T2bb.conditionDescription 				= None
	T2bb.condition 							= None
	T2bb.source 							= 'ATLAS'
	#+++++++ next mass plane block ++++++++++++++
	T2bb_1 									= T2bb.addMassPlane(2*[[x, y]])
	T2bb_1.figure 							= 'Fig.8'
	T2bb_1.figureUrl 						= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-15/fig_08.png'
	T2bb_1.dataUrl 							= 'https://www.hepdata.net/record/ins1623207?version=7&table=Observed exclusion contour directTT'
	T2bb_1.setSources(dataLabels 			= ['expExclusion', 'obsExclusion', 'efficiencyMap'],
								dataFiles 	= ['orig/ExpectedexclusioncontourdirectTT.csv', 'orig/ObservedexclusioncontourdirectTT.csv', 'orig/EffMap_T2tt_' + SR[i] + '.txt'],
								coordinates = [ {x: 0, y: 1, 'value': None}, {x: 0, y: 1, 'value': None},  {x : 1, y: 0, 'value' :2} ],																	 
								dataFormats	= ['csv', 'csv', 'txt'])

'''

databaseCreator.create()
