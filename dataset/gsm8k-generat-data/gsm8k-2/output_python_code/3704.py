def solution():
    """One of the activities in Grade 6 PE class is to get the average weight of the students from each group. In one of the groups, the average weight of five girls is 45 kg while the average weight of five boys is 55 kg. What is the average weight of the ten students from that group?"""
    girls_weight = 45
    boys_weight = 55
    total_weight = (girls_weight * 5) + (boys_weight * 5)
    average_weight = total_weight / 10
    result = average_weight
    return result

print(solution())