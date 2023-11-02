def solution():
    # Calculate the total number of water bottles needed for the road trip
    num_people = 4
    total_hours = 8 + 8
    bottles_per_hour = num_people * 0.5
    total_bottles = total_hours * bottles_per_hour
    result = total_bottles
    return result

print(solution())