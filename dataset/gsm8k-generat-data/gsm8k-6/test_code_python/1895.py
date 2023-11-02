def solution():
    # Calculate the total kilometers ridden by Natalia
    monday_distance = 40  # kilometers ridden on Monday
    tuesday_distance = 50  # kilometers ridden on Tuesday
    wednesday_distance = 0.5 * tuesday_distance  # Wednesday distance is 50% fewer than Tuesday distance
    thursday_distance = monday_distance + wednesday_distance  # Thursday distance is the sum of Monday and Wednesday distances
    total_distance = monday_distance + tuesday_distance + wednesday_distance + thursday_distance  # total distance is the sum of all distances
    result = total_distance
    return result

print(solution())