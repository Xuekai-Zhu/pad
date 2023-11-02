def solution():
    """One of the activities in Grade 6 PE class is to get the average weight of the students from each group. In one of the groups, the average weight of five girls is 45 kg while the average weight of five boys is 55 kg. What is the average weight of the ten students from that group?"""
    # Find the total weight of the girls
    total_girls_weight = 5 * 45

    # Find the total weight of the boys
    total_boys_weight = 5 * 55

    # Find the total weight of all the students
    total_weight = total_girls_weight + total_boys_weight

    # Find the average weight of all the students
    average_weight = total_weight / 10

    # Return the result
    return average_weight

print(solution())