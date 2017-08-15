"""
NCL Functions and Resources Updater for Sublime Text 3
@author: zamlty
@version: 2017.08.15
"""

from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
import requests
import time


def bs(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    return soup

def distinct(L, key=None):
    return sorted(list(set(L)), key=key)

def getTrigger(args):
    func, url = args
    soup = bs(url)
    text = soup.pre.text.splitlines()

    for i, row in enumerate(text):
        if "(" in row:
            start = i + 1
        elif ")" in row:
            end = i
            break

    params = [row.strip().split()[0] for row in text[start:end]]
    contents = ", ".join(["${{{}:{}}}".format(i+1, k) for i, k in enumerate(params)])
    trigger = '{{ "trigger": "{0}", "contents": "{0}({1})" }},\n'.format(func, contents)
    return trigger

def getTrigger_debug(args):
    func, url = args
    soup = bs(url)
    text = soup.pre.text.splitlines()

    for i, row in enumerate(text):
        if func+" (" in row:
            start = i + 1
        elif ")" in row:
            end = i
            break

    try:
        params = [row.strip().split()[0] for row in text[start:end]]
    except UnboundLocalError:
        print(func)

def tmLanguageFile(file, mode, items):
    with open("tmLanguage-"+file, mode) as f:
        f.write("|".join(items))

def completionsFile(file, mode, items):
    with open("completions-"+file, mode) as f:
            for i in items:
                f.write('"{}",\n'.format(i))


# functions
print("functions")
soup = bs("http://www.ncl.ucar.edu/Document/Functions/list_alpha.shtml")
tdList = soup.table.select("tr td[valign]")
functions = [td.text.strip() for td in tdList]
funcUrls = ["http://www.ncl.ucar.edu" + td.find(href=True)["href"] for td in tdList]
tmLanguageFile("functions.txt", "w", functions)

# resources
print("resources")
soup = bs("http://www.ncl.ucar.edu/Document/Graphics/Resources/list_alpha_res.shtml")
stList = soup.select("#general_main dl dt a[name] + strong")
resources = [st.string for st in stList]
resources = distinct(resources)
tmLanguageFile("resources.txt", "w", resources)
completionsFile("resources.txt", "w", resources)

# color tables
print("color tables")
soup = bs("http://www.ncl.ucar.edu/Document/Graphics/color_table_gallery.shtml")
ctables = [next(td.strings) for td in soup.select("table[border=1] tr td")]
ctables = distinct(ctables)
completionsFile("ctables.txt", "w", ctables)

# keywords
print("keywords")
soup = bs("http://www.ncl.ucar.edu/Document/Manuals/Ref_Manual/NclKeywords.shtml")
keywords = [a.string for a in soup.pre('a')]
keywords = distinct(keywords, key=str.lower)
completionsFile("keywords.txt", "w", keywords)

# named colors
print("named colors")
r = requests.get("http://www.ncl.ucar.edu/Applications/Scripts/rgb.txt")
colors = [c[11:].strip() for c in r.text.splitlines()[1:]]
colors = sorted(colors)
completionsFile("colors.txt", "w", colors)

# function completions
print("function completions")
t1 = time.time()
pool = Pool(16)
triggers = pool.map(getTrigger, ((func, url) for func, url in zip(functions, funcUrls)))
pool.close()
pool.join()
with open("completions-function.txt", "w") as f:
    for trigger in triggers:
        f.write(trigger)
t2 = time.time()
print("{:.1f} s".format(t2 - t1))
