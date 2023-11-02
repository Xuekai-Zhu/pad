def solution():
    """An aqua park charges $12 admission and $6 for a tour. A group of 10 people goes to the aquarium and takes the tour; while a group of 5 people only goes to the aquarium. How much does the aqua park earn?"""
    admission_price = 12
    tour_price = 6
    group_1_size = 10
    group_2_size = 5
    group_1_cost = admission_price * group_1_size + tour_price * group_1_size
    group_2_cost = admission_price * group_2_size
    total_earnings = group_1_cost + group_2_cost
    result = total_earnings
    return result

print(solution())