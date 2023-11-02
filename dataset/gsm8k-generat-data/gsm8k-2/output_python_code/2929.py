def solution():
    """An aqua park charges $12 admission and $6 for a tour. A group of 10 people goes to the aquarium and takes the tour; while a group of 5 people only goes to the aquarium. How much does the aqua park earn?"""
    group1_cost = 12 + 6
    group2_cost = 12
    group1_size = 10
    group2_size = 5
    total_earnings = (group1_cost * group1_size) + (group2_cost * group2_size)
    result = total_earnings
    return result

print(solution())