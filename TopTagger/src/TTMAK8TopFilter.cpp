#include "TopTagger/TopTagger/include/TTMAK8TopFilter.h"

#include "TopTagger/TopTagger/include/TopTaggerResults.h"
#include "TopTagger/CfgParser/include/Context.hh"
#include "TopTagger/CfgParser/include/CfgDocument.hh"

void TTMAK8TopFilter::getParameters(const cfg::CfgDocument* cfgDoc, const std::string& localContextName)
{
    //Construct contexts
    cfg::Context commonCxt("Common");
    cfg::Context localCxt(localContextName);
    
    dRMatch_ = cfgDoc->get("dRMatch", commonCxt, -999.9);
}

void TTMAK8TopFilter::run(TopTaggerResults& ttResults)
{
    //Get list of constituents used to construct tops
    const std::vector< Constituent>& constituents = ttResults.getConstituents();
    //Get the list of top candidates as generated by the clustering algo
    std::vector<TopObject>& topCandidates = ttResults.getTopCandidates();
    //Get the list of final tops into which we will stick candidates
    std::vector<TopObject*>& tops = ttResults.getTops();
    //This container will kep trach of which jets have been included in final tops
    std::set<Constituent const *>& usedJets = ttResults.getUsedConstituents();

    //This class adds the merged objects to the final top list 
    for(auto& topCand : topCandidates)
    {
        //For now this just adds the merged tops
        if(topCand.getNConstituents() == 1 && constituentsAreUsed(topCand.getConstituents(), usedJets, dRMatch_))
        {
            tops.push_back(&topCand);
            markConstituentsUsed(topCand.getConstituents(), constituents, usedJets, dRMatch_);
        }
    }    
}
