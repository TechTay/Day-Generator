import random
from unittest import result
from xmlrpc.client import Boolean




Day_Trip_Lists = ['Destinations', 'restaurants', 'mode of transportation', 'entertainment']

destination = ['Hawaii ' ,'Florida ', 'California ', 'Connecticut ', 'Oklahoma', 'New York']
random.choice(destination)


restaurant = ['Popeyes', 'Steakhouse', 'Cajun', 'McDonalds', 'KFC', 'Chipotle']
random.choice(restaurant)


mode_of_transportation = ['Airplane', 'Car', 'Boat', 'Train', 'Biking','Scooter' ]
random.choice(mode_of_transportation)

entertainment = ['Festival', 'Carnival', 'Museum', 'Six Flags', 'Theatre', 'Sporting Event']
random.choice(entertainment)


def day_trip_generator():
    location = random.choice(destination)
    return location

result_of_location = day_trip_generator()
print(f'Destination: {result_of_location} ')

day_trip_generator()

def food_places_generator():
    food = random.choice(restaurant)
    return food

result_of_food = food_places_generator()
print(f'Restaurant: {result_of_food} ')

food_places_generator()

def transportation_generator():
    transportation = random.choice(mode_of_transportation)
    return transportation

result_of_transportation = transportation_generator()
print(f'Transportation: {result_of_transportation} ')

transportation_generator()

def entertainment_generator():
    your_entertainment = random.choice(entertainment)
    return your_entertainment

result_of_entertainment = entertainment_generator()
print(f'Entertainment: {result_of_entertainment} ')

entertainment_generator()

def All_items_generator():
    con_boolean = True
    while con_boolean:
        user_input = input(f'Are you satisfied with your trip? Y or N' '\n')
    if user_input == 'Y':
        All_items_generator()
    All_items = random.choice(day_trip_generator, entertainment_generator,transportation_generator, food_places_generator)
    return All_items


    
    

       
# if location == 'N'
# else:
#             print(f'Destination: {location} ')
        

# x = input('Are you satisfied with your trip? Y or N ' '\n')

# if x == "N '\n' ":
#     print()
# else:
        
#     print(f'Here is your final trip!{All_items_generator}')



