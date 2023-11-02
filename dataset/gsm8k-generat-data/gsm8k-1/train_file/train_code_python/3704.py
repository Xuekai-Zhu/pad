def solution():
    """
    One of the activities in Grade 6 PE class is to get the average weight of the students from each group. In one of the groups, the average weight of five girls is 45 kg while the average weight of five boys is 55 kg. What is the average weight of the ten students from that group?
    """
    num_of_girls = 5
    num_of_boys = 5
    avg_weight_girls = 45
    avg_weight_boys = 55
    total_weight = (num_of_girls * avg_weight_girls) + (num_of_boys * avg_weight_boys)
    avg_weight = total_weight / (num_of_girls + num_of_boys)
    result = avg_weight
    return result

print(solution())