import matplotlib.pyplot as plt
import pickle
import numpy as np

#files =  ["roc_rf_nominal.pkl", "roc_rf_csvSort.pkl", "roc_rf_csvSort_dRPt.pkl", "roc_rf_csvSort_dRPt_n2.pkl", "roc_rf_TeamAVars.pkl"]#, "roc_mlp_TeamAVars.pkl", "roc_mlp_nominal.pkl"]
#labels = ["RF Nominal",         "RF CSV Sort",        "RF CSV Sort + dRPt",      "RF CSV Sort + dRPt + n2",    "RF Team A vars"]#,       "MLP Team A vars",       "MLP Nominal"]

#files =  ["roc_rf_nominal.pkl", "roc_rf_csvSort_dRPt_n2.pkl", "roc_rf_TeamAVars.pkl", "roc_mlp_nominal.pkl", "roc_mlp_csvSort_dRPt_n2.pkl", "roc_mlp_TeamAVars.pkl"]
#labels = ["RF Nominal",         "RF CSV Sort + dRPt + n2",    "RF Team A vars",       "MLP Nominal",         "MLP CSV Sort + dRPt + n2",    "MLP Team A vars"]

#files =  ["roc_mlp_nominal.pkl", "roc_mlp_nominal_2.pkl", "roc_mlp_nominal_3.pkl"]
#labels = ["MLP Nominal 1",       "MLP Nominal 2",         "MLP Nominal 3"]

#files =  ["roc_mlp_TeamAVars.pkl", "roc_mlp_TeamAVars_2.pkl", "roc_mlp_TeamAVars_3.pkl"]
#labels = ["MLP Team A 1",         "MLP Team A 2", "MLP TeamA 3"]

#files =  ["roc_mlp_nominal_dRVars.pkl", "roc_mlp_nominal_dRVars_2.pkl", "roc_mlp_nominal_dRVars_3.pkl", "roc_mlp_nominal_dRVars_4.pkl"]
#labels = ["MLP Nom + dR Vars",          "MLP Nom + dR Vars 2",          "MLP Nom + dR Vars 3",          "MLP Nom + dR Vars 4"]

#files =  ["roc_mlp_nominal_2.pkl", "roc_mlp_TeamAVars_3.pkl", "roc_mlp_nominal_dRVars_3.pkl", "roc.pkl"]
#labels = ["MLP Nominal 2",         "MLP TeamA 3",             "MPL Nominal + dR Vars 3",      "New"]

inputs = {"rf_2bseed": {"files":  ["roc_rf_2bseed_teamAlpha.pkl", "roc_rf_2bseed_teamA.pkl", "roc_rf_2bseed_mixedvars.pkl"],# "roc_rf_2bseed_TeamA_noPtWgt.pkl", "roc_rf_2bseed_TeamAlpha_noPtWgt.pkl"],
                        "labels": ["Team Alpha",                  "Team A",                  "Mixed",                     ],#  "Team Alpha no pT wgt",            "Team A no pT wgt"]
                    },
#          "xgb_2bseed": {"files":  ["roc_xgb_2bseed_TeamAlpha.pkl", "roc_xgb_2bseed_TeamA.pkl"],# "roc_xgb_2bseed_TeamA_noPtWgt.pkl", "roc_xgb_2bseed_TeamAlpha_noPtWgt.pkl"],
#                         "labels": ["Team Alpha",                   "Team A",                 ],#  "Team Alpha no pT wgt",             "Team A no pT wgt"]
#                     },
          "MVAcomp": {"files":  ["roc_xgb.pkl", "roc_rf.pkl",   "roc_mlp.pkl"],
                      "labels": ["xgboot",      "random forest", "Multi-layer perceptron"]
                  },
          "rf_nomSel": {"files":  ["RF_TeamA_Nominal/roc.pkl", "RF_Mixed_Nominal/roc.pkl", "RF_TeamAlpha_Nominal/roc.pkl", "RF_TeamAMoreQGL_Nominal/roc.pkl", "RF_TeamAlphaMoreQGL_Nominal/roc.pkl"],
                        "labels": ["Team A",  "Mixed Variables",         "Team Alpha",           "A + QGL vars",   "Alpha + QGL Vars"],
                    },
          "rf_withZ": {"files":  ["RF_TeamA_Nominal/roc.pkl", "RF_TeamAlpha_Nominal/roc.pkl", "RF_TeamA_NominalWithZ/roc.pkl", "RF_TeamAlpha_NominalWithZ/roc.pkl"],
                       "labels": ["Team A top only",           "Team Alpha top only", "Team A top + Z",           "Team Alpha top + Z"]
                    },
}
          

colors = ["red", "blue", "green", "orange", "black", "purple", "yellow"]

for name, filelist in inputs.iteritems():
    plt.clf()
    ax = plt.figure()
    
    files = filelist["files"]
    labels = filelist["labels"]

    for label, file, color in zip(labels, files, colors):
        f1 = open(file, "rb")
        
        TPR = pickle.load(f1)
        FPR = pickle.load(f1)
        FPRZ = pickle.load(f1)
    
        TPRPtCut = pickle.load(f1)
        FPRPtCut = pickle.load(f1)
        FPRZPtCut = pickle.load(f1)
    
        plt.plot(FPR, TPR, label=label, color=color, alpha=0.6)
        plt.plot(FPRPtCut, TPRPtCut, label=label+" Pt cut", linestyle="dotted", color=color, alpha=0.8)
    
    plt.legend(loc="lower right")
    plt.xlabel("FPR (ttbar)")
    plt.ylabel("TPR (ttbar)")
    plt.savefig("roc_%s.png"%name)
    plt.savefig("roc_%s.pdf"%name)
    plt.close()

    plt.clf()
    ax = plt.figure()
    
    files = filelist["files"]
    labels = filelist["labels"]

    for label, file, color in zip(labels, files, colors):
        f1 = open(file, "rb")
        
        TPR = pickle.load(f1)
        FPR = pickle.load(f1)
        FPRZ = pickle.load(f1)
    
        TPRPtCut = pickle.load(f1)
        FPRPtCut = pickle.load(f1)
        FPRZPtCut = pickle.load(f1)
    
        plt.plot(FPRZ, TPR, label=label, color=color, alpha=0.6)
        plt.plot(FPRZPtCut, TPRPtCut, label=label+" Pt cut", linestyle="dotted", color=color, alpha=0.8)
    
    plt.legend(loc="lower right")
    plt.xlabel("FPR (Znunu)")
    plt.ylabel("TPR (ttbar)")
    plt.savefig("rocZ_%s.png"%name)
    plt.savefig("rocZ_%s.pdf"%name)
    plt.close()
    
