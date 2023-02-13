# James' The Boredless Tourist
 A Project from Codecademy that I worked on

 This code creates a travel recommendation system for various destinations, travelers, and attractions. It starts with defining two functions, get_destination_index(destination) and get_traveler_location(traveler), that find the index of a given destination in the destinations list, and the index of the destination that a traveler is visiting, respectively.

It then defines a list of empty lists, attractions, where each sub-list represents a destination, and the elements in each sub-list are attractions in that destination.

Next, it defines a function add_attraction(destination, attraction) that appends a new attraction to the list of attractions for the specified destination.

After that, it defines a function find_attractions(destination, interests) that finds all the attractions in a given destination that match the interests of a traveler.

Finally, it defines a function get_attractions_for_traveler(traveler) that returns a string of recommended attractions for a given traveler based on their interests and the destination they are visiting.

The code calls get_attractions_for_traveler() for a sample traveler and prints the returned string. It then calls the same function for another traveler and prints the returned string.