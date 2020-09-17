# CHAPTER 1: Using iterators in PythonLand


# Iterators vs Iterables
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

for person in flash:
    print(person)
     
superhero = iter(flash)

print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

small_value = iter(range(3))

print(next(small_value))
print(next(small_value))
print(next(small_value))

for num in range(3):
    print(num)
    
googol = iter(range(10 ** 100))

print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

# Iterators as function arguments
values = range(10, 21)
print(values)

values_list = list(values)
print(values_list)

values_sum = sum(values)
print(values_sum)


# Using enumerate
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']

mutant_list = list(enumerate(mutants))
print(mutant_list)

for index1, value1 in enumerate(mutants):
    print(index1, value1)
    
for index2, value2 in enumerate(mutants, start = 1):
    print(index2, value2)


# Using zip

mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data)

mutant_zip = zip(mutants, aliases, powers)
print(mutant_zip)

for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)


# Using* and zip to 'unzip'

mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']

powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

z1 = zip(mutants, powers)
print(z1)

zi= zip(mutants, powers)
result1, result2 = zip(*z1)

print(result1 == mutants)
print(result2 == powers)

# Processing large amounts of Twitter data
import pandas as pd
tweets_url = 'https://assets.datacamp.com/production/repositories/464/datasets/82e9842c09ad135584521e293091c2327251121d/tweets.csv'

counts_dict = {}

for chunk in pd.read_csv(tweets_url, chunksize=10):
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

print(counts_dict)

# Exacting information for large amounts of Twitter data

def count_entries(csv_file, c_size, colname):
    counts_dict= {}
    
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
  
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
           
        return counts_dict
result_counts = count_entries(tweets_url, 10, 'lang')
print(result_counts)





# CHAPTER 2: List comprehensions and generators
squares = [i**2 for i in range(0, 10)]

matrix = [[col for col in range(0, 5)] for row in range(0, 5)]

for row in matrix:
    print(row)


# Using conditionals in comprehensions
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

new_fellowship2 = [member if len(member) >= 7 else member.replace(member, '') for member in fellowship]
print(new_fellowship2)


# Dict comprehensions
new_fellowship3 = {member : len(member) for member in fellowship}
print(new_fellowship3)


# Write your own generator expressions
result = (num for num in range(31))

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

for value in result:
    print(value)
    

# Changing the output in generator expressions
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

lengths = (len(person) for person in lannister)

for value in lengths:
    print(value)


# Build a generator
def get_lengths(input_list):
    for person in input_list:
        yield len(person)
        
for value in get_lengths(lannister):
    print(value)


# List comprehensions for time-stamped data
df = pd.read_csv('https://assets.datacamp.com/production/repositories/464/datasets/82e9842c09ad135584521e293091c2327251121d/tweets.csv')

tweet_time = df['created_at']
tweet_clock_time = [entry[11:19] for entry in tweet_time]
print(tweet_clock_time)


# conditional list comprehensions for time-stamped data
tweet_exact_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
print(tweet_exact_clock_time)



# CHAPTER 3: Bringing it all together
world_ind_pop_data_url = 'https://assets.datacamp.com/production/repositories/464/datasets/2175fef4b3691db03449bbc7ddffb740319c1131/world_ind_pop_data.csv'

feature_names = ['CountryName', 'CountryCode', 'IndicatorName', 'IndicatorCode', 'Year', 'Value']

row_vales = ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']

zipped_lists = zip(feature_names, row_vales)

rs_dict = dict(zipped_lists)
print(rs_dict)


def lists2dict(list1, list2):
    zipped_lists = zip(list1, list2)
    rs_dict = dict(zipped_lists)
    return rs_dict

rs_fxn = lists2dict(feature_names, row_vales)
print(rs_fxn)

 
row_lists = [['Arab World',
  'ARB',
  'Adolescent fertility rate (births per 1,000 women ages 15-19)',
  'SP.ADO.TFRT',
  '1960',
  '133.56090740552298'],
 ['Arab World',
  'ARB',
  'Age dependency ratio (% of working-age population)',
  'SP.POP.DPND',
  '1960',
  '87.7976011532547'],
 ['Arab World',
  'ARB',
  'Age dependency ratio, old (% of working-age population)',
  'SP.POP.DPND.OL',
  '1960',
  '6.634579191565161'],
 ['Arab World',
  'ARB',
  'Age dependency ratio, young (% of working-age population)',
  'SP.POP.DPND.YG',
  '1960',
  '81.02332950839141'],
 ['Arab World',
  'ARB',
  'Arms exports (SIPRI trend indicator values)',
  'MS.MIL.XPRT.KD',
  '1960',
  '3000000.0'],
 ['Arab World',
  'ARB',
  'Arms imports (SIPRI trend indicator values)',
  'MS.MIL.MPRT.KD',
  '1960',
  '538000000.0'],
 ['Arab World',
  'ARB',
  'Birth rate, crude (per 1,000 people)',
  'SP.DYN.CBRT.IN',
  '1960',
  '47.697888095096395'],
 ['Arab World',
  'ARB',
  'CO2 emissions (kt)',
  'EN.ATM.CO2E.KT',
  '1960',
  '59563.9892169935'],
 ['Arab World',
  'ARB',
  'CO2 emissions (metric tons per capita)',
  'EN.ATM.CO2E.PC',
  '1960',
  '0.6439635478877049'],
 ['Arab World',
  'ARB',
  'CO2 emissions from gaseous fuel consumption (% of total)',
  'EN.ATM.CO2E.GF.ZS',
  '1960',
  '5.041291753975099'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (% of total)',
  'EN.ATM.CO2E.LF.ZS',
  '1960',
  '84.8514729446567'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (kt)',
  'EN.ATM.CO2E.LF.KT',
  '1960',
  '49541.707291032304'],
 ['Arab World',
  'ARB',
  'CO2 emissions from solid fuel consumption (% of total)',
  'EN.ATM.CO2E.SF.ZS',
  '1960',
  '4.72698138789597'],
 ['Arab World',
  'ARB',
  'Death rate, crude (per 1,000 people)',
  'SP.DYN.CDRT.IN',
  '1960',
  '19.7544519237187'],
 ['Arab World',
  'ARB',
  'Fertility rate, total (births per woman)',
  'SP.DYN.TFRT.IN',
  '1960',
  '6.92402738655897'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions',
  'IT.MLT.MAIN',
  '1960',
  '406833.0'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions (per 100 people)',
  'IT.MLT.MAIN.P2',
  '1960',
  '0.6167005703199'],
 ['Arab World',
  'ARB',
  'Hospital beds (per 1,000 people)',
  'SH.MED.BEDS.ZS',
  '1960',
  '1.9296220724398703'],
 ['Arab World',
  'ARB',
  'International migrant stock (% of population)',
  'SM.POP.TOTL.ZS',
  '1960',
  '2.9906371279862403'],
 ['Arab World',
  'ARB',
  'International migrant stock, total',
  'SM.POP.TOTL',
  '1960',
  '3324685.0']]
  
print(row_lists[0])
print(row_lists[1])

list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

print(list_of_dicts[0])
print(list_of_dicts[1])


df = pd.DataFrame(list_of_dicts)
print(df.head())

with open('world_ind_pop_data.csv') as file:
    file.readline()
    counts_dict = {}
    
    for j in range(0, 1000):
        line = file.readline().split(',')
        first_col = line[0]
        
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1
            
print(counts_dict)


def read_large_file(file_object):

    while True:
        data = file_object.readline()
        if not data:
            break
        yield data
        
with open('world_dev_ind.csv') as file:
    gen_file = read_large_file(file)
  
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

counts_dict = {}

with open('world_dev_ind.csv') as file:

    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

       
print(counts_dict)

# Writing an iterator to load data in chunks 

df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

print(next(df_reader))
print(next(df_reader))


urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

df_urb_pop = next(urb_pop_reader)
print(df_urb_pop.head())

df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

pops_list = list(pops)

print(pops_list)

urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()


urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

data = pd.DataFrame()

for df_urb_pop in urb_pop_reader:

    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    pops_list = list(pops)

    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    

    data = data.append(df_pop_ceb)

data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()


def plot_pop(filename, country_code):

    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    data = pd.DataFrame()
    

    for df_urb_pop in urb_pop_reader:

        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

      
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

  
        pops_list = list(pops)

    
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
      
        data = data.append(df_pop_ceb)

    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

fn = 'ind_pop_data.csv'

plot_pop('ind_pop_data.csv', 'CEB')

plot_pop('ind_pop_data.csv', 'ARB')





