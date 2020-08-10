import json
import re
import functools
from collections import Counter
import operator
import nltk
nltk.download('names')
from nltk.corpus import names

def counter_wrapper(c, key):
    if c.get(key) is None:
        return 0
    return c.get(key)

def is_male_story(plot):
    plot = plot.split(" ")
    plot = [re.sub(r'[^\w\s]', '', s) for s in plot]
    plot = [ s.lower() for s in plot]
    c = Counter(plot)
    male_signs_str = ["he", "his", "him", "man", "men", "brother", "brothers",
                      "father", "fathers", "king", "kings","cowboy", "cowboys",
                      "boy", "boys", "son"]
    female_signs_str =["she", "her", "women", "woman", "sister", "sisters", "mother",
                       "mothers","daughter", "queen", "queens", "lady"]

    male_count = functools.reduce(operator.add,
                                   [counter_wrapper(c, name) for name in male_signs_str])
    female_count = functools.reduce(operator.add,
                                   [counter_wrapper(c, name) for name in female_signs_str])

    male_names = [s.lower() for s in names.words('male.txt')]
    female_names = [s.lower() for s in names.words('female.txt')]

    male_count += functools.reduce(operator.add,
                                   [counter_wrapper(c, name) for name in male_names])
    female_count += functools.reduce(operator.add,
                                     [counter_wrapper(c, name) for name in female_names])



    return male_count >= female_count

def open_json_file(name):
    with open(name) as json_file:
        return json.load(json_file)

def get_fairy_tale_plot():
    plots = []
    for arr in open_json_file("./fairyTalesPlots.json"):
        plots.append(arr['plot'])
    return plots

movies_plots = open_json_file("./moviesPlots.json")
fairy_tales_plots = get_fairy_tale_plot()

def count_gender(plots) :    
    male_counter = 0 
    female_counter = 0
    plot_counter = len(plots)
    for plot in plots:
        if is_male_story(plot):
            male_counter+=1
        else:
            female_counter+=1 
    return (male_counter, female_counter, plot_counter)

movies_counter = count_gender(movies_plots)
fairy_tales_counter = count_gender(fairy_tales_plots)

movies_male_prob = movies_counter[0] / movies_counter[2]
movies_female_prob = movies_counter[1] / movies_counter[2]
fairy_tales_male_prob = fairy_tales_counter[0] / fairy_tales_counter[2]
fairy_tales_female_prob = fairy_tales_counter[1] / fairy_tales_counter[2]
print("movies gender prob (male, female)"+ str((movies_male_prob,movies_female_prob)))
print("fairy tales gender prob (male, female)"+ str((fairy_tales_male_prob, fairy_tales_female_prob)))