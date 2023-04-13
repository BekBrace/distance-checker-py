import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, red, yellow

# Declaraing variables (definning the emojis)
walking_emoji = "  🚶"
bus_emoji = "  🚌"
plane_emoji = "  ✈️"

print(blue('Welcome to the distance calculator!\n'))

#Prompt the user for the name of the first city and country
first_city = inquirer.prompt([
    inquirer.Text('name', message='Enter the name of the first city:'),
    inquirer.Text('country', message='Enter the name of the first country:')
])

#Prompt the user for the name of the second city and country
second_city = inquirer.prompt([
    inquirer.Text('name', message='Enter the name of the second city:'),
    inquirer.Text('country', message='Enter the name of the second country:')
])

#Get the latitude and longitude of the first city and country
first_location = f"{first_city['name']}, {first_city['country']}"
first_coords = geocoders.Nominatim(user_agent="distance_calculator").geocode(first_location).point

#Get the latitude and longitude of the second city and country
second_location = f"{second_city['name']}, {second_city['country']}"
second_coords = geocoders.Nominatim(user_agent="distance_calculator").geocode(second_location).point


# Calculate the distance between the two locations
walk_distance = distance.distance(first_coords, second_coords).km
bus_distance = distance.distance(first_coords, second_coords).km
air_distance = distance.distance(first_coords, second_coords).km

#calculate the time to walk the distance
walk_time = walk_distance / 5 

#Calculate for the bus
bus_time = bus_distance / 60
 
#calculate for the airplane
air_time = air_distance / 800


#Print the results
print(green('\nResults:'))

print(f"Distance between {first_location} and {second_location} by:")

print(yellow(f" {walking_emoji} Walking: {walk_distance:.2f} Km, time: {walk_time:.2f} hours"))

print(yellow(f" {bus_emoji} Bus: {bus_distance:.2f} Km, time: {bus_time:.2f} hours"))

print(yellow(f" {plane_emoji} Airplane: {air_distance:.2f} Km, time: {air_time:.2f} hours"))