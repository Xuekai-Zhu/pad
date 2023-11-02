def solution():
    # Calculate the total number of people in Matt's family
    total_people = 1 + 1 + 1 + 1 + 1 + 4 + 2 + 2 + 3 + 3  # Matt, his parents, his brother and his wife, his brother's 4 kids, Uncle Joe and his wife, and their 3 kids
    # Calculate the number of people who can't sleep inside the house
    outside_sleepers = total_people - 4
    # Calculate the number of tents needed for everyone to sleep
    tents_needed = (outside_sleepers // 2) + (outside_sleepers % 2)
    result = tents_needed
    return result

print(solution())