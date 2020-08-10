from textblob import TextBlob
import json

def openJsonFile(name):
    with open(name) as json_file:
        return json.load(json_file)

def getFilesMovies():
    return openJsonFile("./moviesPlots.json")

def getFilesFairy():
    fairys = []
    for arr in openJsonFile("./fariyTalesPlots.json"):
        fairys.append(arr['plot'])
    return fairys

def getAnalysis(semantics):
    
    numOfSem = len(semantics)
    positiveCounter = 0
    negativeCounter = 0
    neutralCounter = 0
    for score in semantics:
        if score < 0:
            negativeCounter+=1
        elif score == 0:
            neutralCounter+=1
        else:
            positiveCounter+=1
        
    return [positiveCounter/numOfSem , neutralCounter/numOfSem, negativeCounter/numOfSem ]

plots_movies = getFilesMovies()
plot_fariys = getFilesFairy()
semantics_movies = []
semantics_fairys = []

for plot in plots_movies:

    semantics_movies.append(TextBlob(plot).sentiment.polarity)
    

print("Family Movies Semantics: " + json.dumps(getAnalysis(semantics_movies)))

for plot in plot_fariys:
    
    semantics_fairys.append(TextBlob(plot).sentiment.polarity)
    

print("Fariy Tales Semantics: " +json.dumps(getAnalysis(semantics_fairys)))
