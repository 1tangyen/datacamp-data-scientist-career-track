# Write a simple function


def shout():
    shout_word = "congratulations" + "!!!"
    print(shout_word)


shout()

# Single-parameter functions
def shout(word):
    shout_word = word + "!!!"
    print(shout_word)


shout("congratulations")


# Functions that return single values
def shout(word):
    shout_word = word + "!!!"
    return shout_word


yell = shout("congratulations")
print(yell)


# Functions with multiple parameters
def shout(word1, word2):
    shout1 = word1 + "!!!"
    shout2 = word2 + "!!!"
    new_shout = shout1 + shout2
    return new_shout


yell = shout("congratulations", "you")
print(yell)


# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    shout1 = word1 + "!!!"
    shout2 = word2 + "!!!"
    shout_words = (shout1, shout2)
    return shout_words


yell1, yell2 = shout_all("congratulations", "you")
print(yell1)
print(yell2)


import pandas as pd

df = pd.read_csv(
    "https://assets.datacamp.com/production/repositories/463/datasets/82e9842c09ad135584521e293091c2327251121d/tweets.csv"
)

# Bringing it all together

langs_count = {}
col = df["lang"]

for entry in col:
    if entry in langs_count.keys():
        langs_count[entry] += 1
    else:
        langs_count[entry] = 1
print(langs_count)

# Bringing it all together2
def count_entries(df, col_name):
    langs_count = {}
    col = df[col_name]
    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1
    return langs_count


result = count_entries(df, "lang")
print(result)

# Default arguments, variable-length arguments and scope
# The keyword global

team = "teen titans"


def change_team():
    global team
    team = "justice league"


print(team)

change_team()
print(team)


# Nested Functions I
def three_shouts(word1, word2, word3):
    def inner(word):
        return word + "!!!"

    return (inner(word1), inner(word2), inner(word3))


print(three_shouts("a", "b", "c"))



# Nested Funtions II

def echo(n):
    def inner_echo(word1):
        echo_word = word1 * n
        return echo_word
    return inner_echo

twice = echo(2)

thrice = echo(3)

print(twice('hello'), thrice('hello'))

# Functions with one default argument
def shout_echo(word1, echo=1):
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'
    return shout_word
 
no_echo = shout_echo('Hey')
with_echo = shout_echo('Hey', echo = 5)

print(no_echo)
print(with_echo)


# Functions with multiple default arguments
def shout_echo(word1, echo=1, intense=True):
    echo_word = word1 * echo
    if intense is True:
        echo_word_new = echo_word.upper() + '!!!'
    else:
        echo_word_new = echo_word + '!!!'
        
    return echo_word_new
    
with_big_echo = shout_echo('Hey', echo=5, intense=True)
big_no_echo = shout_echo('Hey', intense=True)

print(with_big_echo)
print(big_no_echo)


# Functions with variable-length arguments(*args)
def gibberish(*args):
    hodgepodge = ''
    for word in args:
        hodgepodge += word 
    
    return hodgepodge

one_word = gibberish('luke')

many_words = gibberish('luke', 'leia', 'han', 'obi', 'darth')

print(one_word)
print(many_words)


# Functions with variable-length keyword arguments (*kwargs)
def report_status(**kwargs):
    print('\nBEGIN: REPORT\n')
    
    for key, value in kwargs.items():
        print(key + ': ' + value)
    print('\nEND REPORT')
    
report_status(name = 'luke', affiliation = 'jedi', status = 'missing')

report_status(name = 'anakin', affiliation = 'sith lord', status = 'deceased')


# Bringing it all together
tweets_df = pd.read_csv("https://assets.datacamp.com/production/repositories/463/datasets/82e9842c09ad135584521e293091c2327251121d/tweets.csv")

def count_entries(df, col_name='lang'):
    cols_count = {}
    col = df[col_name]
    for entry in col:
        if entry in cols_count.keys():
            cols_count[entry] += 1
        else:
             cols_count[entry] = 1
    return cols_count
     
result1 = count_entries(tweets_df, col_name='lang')
result2 = count_entries(tweets_df, col_name='source')

print(result1)
print(result2)


# Bringing it all together(2)
def count_entries(df, *args):
    cols_count = {}
    for entry in args:
        col = df[col_name]
        for entry in col:
            if entry in cols_counts.keys():
                cols_count[entry] += 1
            else:
                cols_count[entry] =1
        return cols_count

        
result1 = count_entries(tweets_df, 'lang')
result2 = count_entries(tweets_df, 'lang', 'source')

print(result1)
print(result2)



# Writing a lambda function you already know
echo_word = lambda word1, echo: word1 * echo
result = echo_word('hey', 5)
print(result)

# Map() and lambda functions
spells = ['protego', 'accio', 'expecto patronum', 'legilimens']

shout_spells = map(lambda a:a + '!!!', spells)

shout_spells_list = list(shout_spells)

print(shout_spells_list)

# Filter() and lambda functions
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = filter(lambda member :len(member)>6, fellowship)

result_list = list(result)

print(result_list)

# Reduce() and lambda functions
from functools import reduce
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
result = reduce(lambda item1, item2 : item1+item2, stark)

print(result)

# Error handling with try-except
def shout_echo(word1, echo=1):
    echo_word = ''
    shout_words = ''
    try:
        echo_word = word1 * echo
        shout_words = echo_word + '!!!'
    except:
        print('word1 must be a string and scho must be an integer.')
        
    return shout_words
    
shout_echo('particle', echo='accelerator')

# Error handling by raising an error
def shout_echo(word1, echo=1):
    if echo<0:
        raise ValueError('echo nust be greater than or equal to 0')
    echo_word = word1 * echo
    shout_word = echo_word + '!!!'
    return shout_word
                
shout_echo('practicle', echo=5)  
  
# Bringing it all together
import pandas as pd
tweets_df = pd.read_csv('https://assets.datacamp.com/production/repositories/463/datasets/82e9842c09ad135584521e293091c2327251121d/tweets.csv')
result = filter(lambda x:x[0:2] == 'RT', tweets_df['text'])

res_list = list(result)

for tweet in res_list:
    print(tweet)


def count_entries(df, col_name='lang'):
    cols_count = {}
    try:
        col = df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count[entry] += 1
            else:
                cols_count = 1
        return cols_count
   
    except: 
        return 'The DataFrame does not have a ' + col_name + 'column'
        
result1 = count_entries(tweets_df, 'lang')

print(result1)  
  

def count_entries(df, col_name='lang'):
    if col_name not in df.columns:
        raise ValueError('The DataFrame does no have a ' + colname + ' column.')
        
    cols_count = {}  
    col = df[col_name]
    
    for entry in col:
         if entry in cols_count.keys():
             cols_count[entry] += 1
         else:
             cols_count[entry] = 1
    return cols_count 

result1 = count_entries(tweets_df)

print(result1)  
  
  
  
  
  
  