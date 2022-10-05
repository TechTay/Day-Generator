import random


Day_Trip_Lists = ['Destinations', 'restaurants', 'mode of transportation', 'entertainment']

destination = ['Hawaii ' ,'Florida ', 'California ', 'Connecticut ', 'Oklahoma', 'New York']
random.choice(destination)


restaurant = ['Popeyes', 'Steakhouse', 'Cajun', 'McDonalds', 'KFC', 'Chipotle']
random.choice(restaurant)


mode_of_transportation = ['Airplane', 'Car', 'Boat', 'Train', 'Biking','Scooter' ]
random.choice(mode_of_transportation)

entertainment = ['Festival', 'Carnival', 'Museum', 'Six Flags', 'Theatre', 'Sporting Event']
random.choice(entertainment)


print('\n')
print('Here is your randomized trip!' '\n')

def day_trip_generator():
    location = random.choice(destination)
    return location

result_of_location = day_trip_generator()
print(f'Destination: {result_of_location} ')



def food_places_generator():
    food = random.choice(restaurant)
    return food

result_of_food = food_places_generator()
print(f'Restaurant: {result_of_food} ')


def transportation_generator():
    transportation = random.choice(mode_of_transportation)
    return transportation

result_of_transportation = transportation_generator()
print(f'Transportation: {result_of_transportation} ')


def entertainment_generator():
    your_entertainment = random.choice(entertainment)
    return your_entertainment

result_of_entertainment = entertainment_generator()
print(f'Entertainment: {result_of_entertainment} ' '\n')


def All_items_generator():
    con_boolean = True
    while con_boolean:
        user_input = input(f'Are you satisfied with your trip? Y or N' '\n')
        if user_input == 'Y':
            print('Here is your final trip! ', ' \n' )
            print(f'Entertainment: {result_of_entertainment} ')
            print(f'Destination: {result_of_location} ')
            print(f'Restuarant: {result_of_food} ')
            print(f'Transportation: {result_of_transportation} ')

            con_boolean = False
        
            
        else:
            result_of_no = input(f'What do you not like about your trip? The Destination, Restuarant, Entertainment, or Transportation?' '\n')
            if   result_of_no == 'Destination':
                    result_of_location = day_trip_generator()
            elif result_of_no == "Entertainment":
                    result_of_entertainment = entertainment_generator()
            elif result_of_no == "Restuarant":
                    result_of_food = food_places_generator()
            elif result_of_no == "Transportation":
                    result_of_no = transportation_generator()
                    
                    
        
All_items_generator()

print('Safe Travels!')




