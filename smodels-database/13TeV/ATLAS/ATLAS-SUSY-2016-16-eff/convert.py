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
info 			 = MetaInfoInput('ATLAS-SUSY-2016-16')
info.url 		 = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/'
info.sqrts 		 = 13
info.lumi 		 = 36.1
info.prettyName  = 'stop to lsp + MET'
info.private 	 = False
info.arxiv 		 = 'https://arxiv.org/abs/1711.11520'
info.contact 	 = 'ATLAS collaboration'
info.publication = 'JHEP 06 (2018) 108'




SR   = {'obsN' 	: [8,50,19,115,34,68,70], 
		'expN'  : [3.8,36.3,18.3,115,30.3,71,60.5], 
		'bgErr' : [1,6.6,2.2,31,5.9,16,6.1], 
		'SR' 	: ['tN_high', 'tN_med', 'tN_diag_high', 'tN_diag_med','tN_diag_low','bWN','bffN'],
    'NsigUL' : [10.0,31.0,11.0,58.0,17.0,31.0,28.0],
    'NsigULexp' : [5.8,19.0,11.0,58.0,19.0,33.0,21.0]}


T2tt = {
'name' 		 : 'T2tt',
'info' 		 :{'figure' 		: 'Fig.20', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/fig_20.png', 
			   'dataUrl' 		: ['https://www.hepdata.net/record/ins1639856?version=4&table=Table87;https://www.hepdata.net/record/ins1639856?version=4&table=Table88',
                         'https://www.hepdata.net/record/ins1639856?version=4&table=Table89;https://www.hepdata.net/record/ins1639856?version=4&table=Table90']},
'sources' : ['orig/eff_SR.csv','orig/eff_deltaM_SR.csv'],
'constraint' : '[[[t]],[[t]]]',
'massConstr' : None,
'massPlanes'  : [2*[[x, y]],2*[[x,x-y]]]}

T2ttoff = {
'name' 		 : 'T2ttoff',
'info' 		 :{'figure' 		: 'Fig.20', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/fig_20.png', 
			   'dataUrl' 		: ['https://www.hepdata.net/record/ins1639856?version=4&table=Table87;https://www.hepdata.net/record/ins1639856?version=4&table=Table88',
                         'https://www.hepdata.net/record/ins1639856?version=4&table=Table89;https://www.hepdata.net/record/ins1639856?version=4&table=Table90']},
'sources' : ['orig/eff_SR.csv','orig/eff_deltaM_SR.csv'],
'constraint' : '[[[b, W]],[[b, W]]]',
'massConstr' : 2*[['80 <= dm < 169.0']],
'massPlanes'  : [2*[[x, y]],2*[[x,x-y]]]}

T2bbll = {
'name' 		 : 'T2bbll',
'info' 		 :{'figure' 		: 'Fig.20', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-16/fig_20.png', 
			   'dataUrl' 		: ['https://www.hepdata.net/record/ins1639856?version=4&table=Table87;https://www.hepdata.net/record/ins1639856?version=4&table=Table88',
                         'https://www.hepdata.net/record/ins1639856?version=4&table=Table89;https://www.hepdata.net/record/ins1639856?version=4&table=Table90']},

'sources' : ['orig/eff_SR.csv','orig/eff_deltaM_SR.csv'],
'constraint' : '[[[b, L, nu]],[[b, jet,jet]]]',
'massConstr' : [['dm < 80'], ['dm < 80']],
'massPlanes'  : [2*[[x, y]],2*[[x,x-y]]]}

Txnames = [T2tt,T2ttoff,T2bbll]
# Txnames = [T2tt,T2ttoff]

exclusionCurves = {'obs' : ['orig/Table17.csv','orig/Table20.csv'], 'exp' : ['orig/Table16.csv','orig/Table19.csv']}


for i,sr in enumerate(SR['SR']):
	#+++++++ dataset block ++++++++++++++
    dataset = DataSetInput(sr)
    dataset.setInfo(dataType = 'efficiencyMap', dataId = sr, 
                  observedN = SR['obsN'][i], expectedBG = SR['expN'][i], bgError = SR['bgErr'][i],
                  upperLimit = str(SR['NsigUL'][i]/36.1).strip()+'*fb', 
                  expectedUpperLimit = str(SR['NsigULexp'][i]/36.1).strip()+'*fb')
	  #+++++++ next txName block ++++++++++++++
    for TX in Txnames:
        #The SRs 'bffN' and 'tN_diag_low' only apply to T2tt and T2bbll
        if sr in ['bffN','tN_diag_low'] and TX['name'] != 'T2bbll':
            continue
        newTx = dataset.addTxName(TX['name'])
        newTx.checked = 'False'
        newTx.constraint = TX['constraint']
        newTx.conditionDescription = None
        newTx.condition	= None
        newTx.source = 'ATLAS'
        newTx.massConstraint = TX['massConstr']
        for ip,plane in enumerate(TX['massPlanes']):
            if not os.path.isfile(TX['sources'][ip].replace('SR',sr)):
                continue
            #+++++++ next mass plane block ++++++++++++++
            newPlane = newTx.addMassPlane(plane)
            newPlane.figure = TX['info']['figure']
            newPlane.figureUrl = TX['info']['figureUrl']
            newPlane.dataUrl = TX['info']['dataUrl']
            newPlane.addSource('efficiencyMap', TX['sources'][ip].replace('SR',sr), 'csv')
            newPlane.addSource('obsExclusion', exclusionCurves['obs'][ip], 'csv')
            newPlane.addSource('expExclusion', exclusionCurves['exp'][ip], 'csv')
            newTx.addMassPlane(newPlane)


databaseCreator.create()
