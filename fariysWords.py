import json

fariy_words = ["resolution",	"protagonist"	,"conflict",
"plot",	"goblin",	"prince" ,"charming",
"tiara",	"curse",	"carriage",
"damsel",	"wicked",	"character",
"ogre",	"adventure",	"beanstalk",
"hero",	"weak",	'forest',
"tower",	"enemy"	,"fairy",
"axe"	,"bear"	,"antagonist",
"climax",	"Step-mother"	,"enchantment",
"myth",	"heroine",	"crown",
"tower"	,"fairy", "godmother"	,"maiden"
"wand"	,"glass" ,"slippers"	,"troll",
"drawbridge",	"kiss",	"story"
"villain"	,"cottage",	"horse",
"pig"	,"brave"	,"dwarves",
"dwarf",	"beautiful",	"frog",
"sword"	,"castle",	"elf",
"toad",	"spell"	,"dragon",
"wolf"	,"magic"	,"knight",
"beast"	,"prince"	,"king",
"giant"	,"queen"	,"princess",
"witch",	"once upon a time"	,"good",
"evil",	"fairy tale",	"happily ever after",
"folktale",	"setting"	,"resolution",
"gown"]


def openJsonFile(name):
    with open(name) as json_file:
        return json.load(json_file)

def get_fairy_tale_plot():
    plots = ""
    for arr in openJsonFile("./fariyTalesPlots.json"):
        plots += arr['plot']
    return plots
    
def getFiles():
    plots = ""
    for arr in openJsonFile("./moviesPlots.json"):
       plots += arr
    return plots

plots_movies = getFiles()
plots_movies_str = json.dumps(plots_movies)

plots_fariy = get_fairy_tale_plot()
plots_fariy_str = json.dumps(plots_fariy)

def countWords(plots_str , limit):
    words_counter = {}
    for i in fariy_words:
        words_counter[i.lower()]= 0
    words = str(plots_str).split(' ')
    for word_movie in words:
        for word_fariy in fariy_words:
            if word_movie.lower() == word_fariy:
                words_counter[word_fariy.lower()]+=1
            elif word_movie.lower() == word_fariy+"es":
                words_counter[word_fariy.lower()]+=1
            elif word_movie.lower() == word_fariy+"s":
                words_counter[word_fariy.lower()]+=1
    numOfWords = len(plots_str)
    finall = {}       
    for word in words_counter:
        if(words_counter[word] > limit):
            finall[word] = words_counter[word]/numOfWords

    print(finall)
countWords(plots_movies_str, 9)
countWords(plots_fariy_str, 50)
