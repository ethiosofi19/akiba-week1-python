# Travel Planner

destination = input("Whats your destination? ")
distance = float(input("Distance in kilometers? "))
ave_speed = float(input("Average speed in km/h? "))

time = distance/ave_speed

print("\nDestination: ",destination)
print("Distance: ",distance,"km")
print("Average Speed:",ave_speed,"km/h\n")
print("Estimated Travel Time: ",int(time),"hours")





