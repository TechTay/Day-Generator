import random



Day_Trip_Lists = ['Destinations', 'restaurants', 'mode of transportation', 'entertainment']

destination = ['Hawaii ' ,'Florida ', 'California ', 'Connecticut ']
random.choice(destination)




restaurant = ['Popeyes', 'Steakhouse', 'Cajun', 'McDonalds']
random.choice(restaurant)


mode_of_transportation = ['Airplane', 'Car', 'Boat', 'Train']
random.choice(mode_of_transportation)

entertainment = ['Festival', 'Carnival', 'Museum', 'Six Flags']
random.choice(entertainment)


def day_trip_generator():
    location = random.choice(destination)
    print(f'Destination: {location} ')

day_trip_generator()

def food_places_generator():
    food = random.choice(restaurant)
    print(f'Restaurant: {food} ')

food_places_generator()

def transportation_generator():
        transportation = random.choice(mode_of_transportation)
        print(f'Transportation: {transportation} ')

transportation_generator()

def entertainment_generator():
    your_entertainment = random.choice(entertainment)
    print(f'Entertainment: {your_entertainment} ')

entertainment_generator()

def All_items_generator():
    All_items = (entertainment_generator + transportation_generator + food_places_generator + day_trip_generator)
    print(f'{All_items} ')

x = input('Are you satisfied with your trip? Y or N ' '\n')

if x == "N '\n' ":
    print(f'need assistance...')
else:
    confirm_trip = False
while confirm_trip:
    break
        
print(f'Here is your final trip!{All_items_generator}')



