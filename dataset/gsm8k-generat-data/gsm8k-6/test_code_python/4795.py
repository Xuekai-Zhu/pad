def solution():
    # Calculate the total time James spends cleaning the house
    bedroom_time = 20 * 3  # time taken to clean all 3 bedrooms
    living_room_time = bedroom_time  # time taken to clean the living room
    bathroom_time = living_room_time * 2  # time taken to clean both bathrooms
    total_house_time = bedroom_time + living_room_time + bathroom_time  # total time taken to clean the house

    # Calculate the time taken to clean the outside
    outside_time = total_house_time * 2

    # Calculate the total time taken to complete all chores
    total_time = (total_house_time + outside_time) / 3  # James splits the chores with his 2 siblings
    total_hours = total_time / 60  # convert minutes to hours
    result = total_hours
    return result

print(solution())