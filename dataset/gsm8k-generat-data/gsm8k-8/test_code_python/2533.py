def solution():
    # Calculate the total number of people going on the vacation
    total_people = 2 + 2 + 2 + 2 + 2 + 4 + 3

    # Calculate the number of people who can sleep in the house
    house_capacity = 4

    # Calculate the number of people who need to sleep in tents
    tent_capacity = total_people - house_capacity

    # Calculate the number of tents needed, assuming 2 people per tent
    tents_needed = tent_capacity // 2

    result = tents_needed
    return result

print(solution())