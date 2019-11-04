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
argparser.add_argument ('-no', '--noUpdate',
help = 'do not update the lastUpdate field.',\
action= "store_true" )
argparser.add_argument ('-r', '--resetValidation',
help = 'reset the validation flag',\
action= "store_true" )
args = argparser.parse_args()

if args.noUpdate:
    os.environ["SMODELS_NOUPDATE"]="1"

if args.resetValidation:
    os.environ["SMODELS_RESETVALIDATION"]="1"

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
from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput, getSignalRegionsEMBaked, getStatsEMBaked
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z



#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2016-07')
info.url = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-07/"
info.sqrts = 13
info.lumi = 36.1
info.prettyName = "hadronic jets + MET"
info.private = False
info.arxiv = 'https://arxiv.org/abs/1712.02332'
info.contact = 'ATLAS collaboration'
info.publication = 'Phys. Rev. D 97, 112001 (2018)'

stats = getStatsEMBaked ()

topos = [ "T1", "T2", "T6WWleft", "T5WW", "T5ZZ", "T5WZh", "T6WZh", "T5WWoff", "T6WWoffleft", "TGQ" ]
# topos = [ "TGQ" ]
#constraints = { "T2": "[[[q]],[[q]]]", "T1": "[[[q,q]],[[q,q]]]", "T6WWleft": "[[['q'],['W']],[['q'],['W']]]", "T6WWoffleft": "2.23 * [[['jet'],['jet','jet']],[['jet'],['jet','jet']]]", "T5WW": "[[['q','q'],['W']],[['q','q'],['W']]]", "T5ZZ": "[[['q','q'],['Z']],[['q','q'],['Z']]]", "T5WZh": "[[[q,q],[Z]],[[q,q],[W]]]+[[[q,q],[higgs]],[[q,q],[W]]]", "T6WZh": "[[[q],[Z]],[[q],[W]]]+[[[q],[higgs]],[[q],[W]]]", "T5WWoff": "2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]", "TGQ": "[[[q]],[[q,q]]]" }
constraints = { "T2": "[[[q]],[[q]]]", "T1": "[[[q,q]],[[q,q]]]", "T6WWleft": "[[['q'],['W']],[['q'],['W']]]", "T6WWoffleft": "2.23 * [[['jet'],['jet','jet']],[['jet'],['jet','jet']]]", "T5WW": "[[['q','q'],['W']],[['q','q'],['W']]]", "T5ZZ": "[[['q','q'],['Z']],[['q','q'],['Z']]]", "T5WZh": "[[[q,q],[Z]],[[q,q],[W]]]+[[[q,q],[higgs]],[[q,q],[W]]]+[[[q,q],[higgs]],[[q,q],[higgs]]]+[[[q,q],[higgs]],[[q,q],[Z]]]", "T6WZh": "[[[jet],[Z]],[[jet],[W]]]+[[[jet],[higgs]],[[jet],[W]]]+[[[jet],[Z]],[[jet],[Z]]]+[[[jet],[higgs]],[[jet],[higgs]]]+[[[jet],[Z]],[[jet],[higgs]]]", "T5WWoff": "2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]", "TGQ": "[[[q]],[[q,q]]]" }

conditions = { "T5WZh": "Csim([[[q,q],[Z]],[[q,q],[W]]]+[[[q,q],[higgs]],[[q,q],[W]]],2.*([[[q,q],[W]],[[q,q],[W]]]))", "T6WZh": "Csim([[[jet],[Z]],[[jet],[W]]]+[[[jet],[higgs]],[[jet],[W]]],2.*([[[jet],[W]],[[jet],[W]]]))" }

figure = { "T2": "Fig. 76a", "T1": "Fig. 76b", "T6WWleft": ('Fig. 77a', 'Fig. 77b' ), "T5WW": ( 'Fig. 77c', 'Fig. 77d' ), "T5ZZ": ('Fig.79', None) , "T5WZh": ('Fig. 78b', None ), "T6WZh":  ('Fig. 78a', None ), "T5WWoff": ( 'Fig. 77c', 'Fig. 77d' ), "T6WWoffleft": ('Fig. 77a', 'Fig. 77b' ), "TGQ": ('Fig. 80a', 'Fig. 80b', 'Fig. 80c' ) }
baseUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-07/'
figureUrl = { "T2": 'figaux_076a.png', "T1": 'figaux_076b.png',
              "T6WWleft": ( 'figaux_077a.png', 'figaux_077b.png' ),
              "T5WW": ( 'figaux_077c.png', 'figaux_077d.png' ),
              "T5WWoff": ( 'figaux_077c.png', 'figaux_077d.png' ),
              "T5WZh": ('figaux_078b.png', None),
              "T6WZh": ('figaux_078a.png', None ),
              "T5ZZ": ('figaux_079.png', None),
              "T6WWoffleft": ( 'figaux_077a.png', 'figaux_077b.png' ),
              "TGQ": ( 'figaux_080a.png', 'figaux_80b.png', 'figaux_80c.png' )
}
dataBaseUrl = "'https://www.hepdata.net/record/ins1641270?version=5&table=X-section U.L. & best SR @@NUM@@  : @@MEFFRJR@@'"
exclusionIndex = { "T2": 1, "T1": 2, "T6WWleft": ( 3, 4 ), "T5WW": (5, 6 ),
                   "T5ZZ": (7, None), "T6WWoffleft": ( 3, 4 ),
                   "T5WZh": (9,None), "T6WZh": (8, None ), "T5WWoff": (5, 6 ),
                   "TGQ": (10,11,12) }
massPlanes = { "T2": 2*[[x, y]], "T1": 2*[[x, y]],
        "T6WWleft": ( 2*[[x, 0.5*(x+y), y]], 2*[[x, y, 60.]]),
        "T6WWoffleft": ( 2*[[x, 0.5*(x+y), y]], 2*[[x, y, 60.]]),
        "T5WZh": (2*[[x, y, 60.]],None),
        "T6WZh": (2*[[x, y, 60.]], None ), "T5ZZ": (2*[[x, y, 1.]], None),
        "T5WW": ( 2*[[x, 0.5*(x+y), y]], 2*[[x, y, 60.]]),
        "T5WWoff": ( 2*[[x, 0.5*(x+y), y]], 2*[[x, y, 60.]]),
        "TGQ": ( [[x,0.],[y, 0.]], [[x, 695.],[y, 695.]], [[x, 995.],[y, 995.]] )
}

datasets={}

dsnames=getSignalRegionsEMBaked("orig/%s.embaked" % "T2" )

for dsname in dsnames:
    #+++++++ dataset block ++++++++++++++
    if not dsname in stats:
        print ( "cannot find stats for %s" % dsname )
        continue
    dataset = DataSetInput( dsname )
    dst = stats[dsname]
    dataset.setInfo(dataType = 'efficiencyMap', dataId = dsname,
         observedN = dst["nobs"], expectedBG = dst["nb"] , bgError = dst["deltanb"] )
    datasets[dsname]=dataset


rjrs = [ 1, 2, 3, 5 ]

for topo in topos:

    for dsname in dsnames:
        #+++++++ next txName block ++++++++++++++
        Tx = datasets[dsname].addTxName( topo )
        Tx.checked = ''
        Tx.constraint = constraints[topo]
        Tx.conditionDescription = None
        Tx.condition = None
        if topo in conditions.keys():
            Tx.condition = conditions[topo]
        Tx.source = "ATLAS"
        #+++++++ next mass plane block ++++++++++++++
        mPlanes = massPlanes[topo]
        if type (mPlanes) == list:
            Tx_1 = Tx.addMassPlane(massPlanes[topo])
            Tx_1.figure = figure[topo]
            Tx_1.figureUrl = baseUrl + figureUrl[topo]
            eIdx = exclusionIndex[topo]
            meffrjr = "Meff"
            meffrjrurl = "Meff"
            if eIdx in rjrs:
                meffrjr = "Meff+RJR"
                meffrjrurl = "Meff%2BRJR"
            Tx_1.dataUrl = dataBaseUrl.replace("@@NUM@@",str(eIdx) ).replace("@@MEFFRJR@@",meffrjrurl )
            expCont = 'orig/Exclusioncontour(exp.)%d:%s.csv' % (eIdx,meffrjr)
            obsCont = 'orig/Exclusioncontour(obs.)%d:%s.csv' % (eIdx,meffrjr)
            units = [ None, None, None ]
            if "60." in str(massPlanes[topo]):
                units = [ ("GeV","X:60"), ("GeV","X:60" ), None ]
            if eIdx in [ 4, 6, 8, 9 ]:
                ulfile = 'orig/UL_SR%d.csv' % eIdx
                expCont = 'orig/expSR%d.csv' % eIdx
                obsCont = 'orig/obsSR%d.csv' % eIdx
            topoon = topo.replace("off","")
            Tx_1.setSources(dataLabels= ['expExclusion', 'obsExclusion', 'efficiencyMap'],
                objectNames = [ None, None, dsname ],
                dataFiles= [ expCont, obsCont, 'orig/%s.embaked' % topoon ],
                units = units,
                dataFormats= ['csv', 'csv', 'embaked'])
        if type (mPlanes) == tuple:
            mArray=2*[[x,y,z]]
            if topo == "TGQ":
                mArray=[[x,z],[y,z]]
            Tx_1 = Tx.addMassPlane(mArray)
            eIdx = exclusionIndex[topo][0]
            topoon = topo.replace("off","")
            Tx_1.setSources(dataLabels= ['efficiencyMap'],
                objectNames = [ dsname ],
                dataFiles= [ 'orig/%s.embaked' % topoon ],
                units = [ None],
                dataFormats= [ 'embaked'] )
            for ctr,mp in enumerate(mPlanes):
                if mp == None:
                    continue
                Tx_m = Tx.addMassPlane(mp)
                Tx_m.figure = figure[topo][0]
                Tx_m.figureUrl = figureUrl[topo][0]
                eIdx = exclusionIndex[topo][ctr]
                meffrjr = "Meff"
                meffrjrurl = "Meff"
                if eIdx in rjrs:
                    meffrjr = "Meff+RJR"
                    meffrjrurl = "Meff%2BRJR"

                Tx_m.dataUrl = dataBaseUrl.replace("@@NUM@@",str(eIdx) ).replace("@@MEFFRJR@@",meffrjrurl )
                expCont = 'orig/Exclusioncontour(exp.)%d:%s.csv' % (eIdx,meffrjr)
                obsCont = 'orig/Exclusioncontour(obs.)%d:%s.csv' % (eIdx,meffrjr)
                units = [ None, None ]
                if "60." in str(mp):
                    units = [ ("GeV","X:60"), ("GeV","X:60" ) ]
                Tx_m.setSources(dataLabels= ['expExclusion', 'obsExclusion' ],
                    objectNames = [ None, None ],
                    dataFiles= [ expCont, obsCont ],
                    units = units,
                    dataFormats= ['csv', 'csv' ])

databaseCreator.create()
