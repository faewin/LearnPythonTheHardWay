# Exercise 39 - Dictionaries, Oh lovely dictionaries

person = {'name': 'Edward', 'age': 25}
print person['name']
print person['age']
person['city'] = 'San Francisco'
print person['city']

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add more cities

cities['NY'] = 'New York'
cities['TX'] = 'Austin'
cities['OR'] = 'Oregon'

# print cities

print "-" * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print "-" * 10
print "Florida's abbreviation is: ", states['Florida']
print "New Yorks's abbreviation is: ", states['New York']

