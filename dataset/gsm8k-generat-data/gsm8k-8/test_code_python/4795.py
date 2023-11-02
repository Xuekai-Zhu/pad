def solution():
    # Calculate the time it takes to clean each bedroom
    bedroom_time = 20

    # Calculate the time it takes to clean the living room
    living_room_time = 3 * bedroom_time

    # Calculate the time it takes to clean each bathroom
    bathroom_time = 2 * living_room_time

    # Calculate the total time to clean the inside of the house
    inside_time = (3 * bedroom_time) + living_room_time + (2 * bathroom_time)

    # Calculate the time it takes to clean the outside of the house
    outside_time = 2 * inside_time

    # Calculate the total time for all three siblings to clean the inside and outside of the house
    total_time = (inside_time + outside_time) / 3

    # Convert the total time to hours and return the result
    result = total_time / 60
    return result

print(solution())