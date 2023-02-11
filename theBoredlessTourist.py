destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cario, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


#print(attractions)

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#get_destination_index("Los Angeles, USA")
#get_destination_index("Paris, France")
#get_destination_index("Hyderabad, India")

def get_traveler_location(traveler):
  traveler_destination =  test_traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError:
    return
   
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
print(attractions)