stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh")
# print(stops) 

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queens St")
# print(stops)

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
# print(stops)

#4. Print out the index position of "Linlithgow"
index = stops.index("Linlithgow")
# print(index)

#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
# print(stops)

#6. Delete "Cumbernauld" from the list by index
del(stops[2])
# print(stops)

#7. Print the number of stops there are in the list
num_of_stops = len(stops)
# print(num_of_stops)
# print(stops)

#8. Sort the list alphabetically
stops.sort()
# print(stops)

#9. Reverse the positions of the stops in the list
stops.reverse()
# print(stops)

#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)




# PythonMethods
# https://docs.python.org/3/tutorial/datastructures.html
# quiz
# https://docs.google.com/forms/d/e/1FAIpQLSc0FNd66FGGdtQMRC6_fx5r3mp6zGA3EP2e1VoImdqS2FcAiA/viewform
