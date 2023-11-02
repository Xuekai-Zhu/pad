def solution():
    """A convenience store sold 100 bags of chips in a month. In the first week, 15 bags of chips were sold. In the second week, thrice as many bags of chips were sold. There was an equal number of chips sold in the third and fourth week. How many chips were sold in the third and fourth week?"""
    total_bags = 100
    first_week_bags = 15
    second_week_bags = 3 * first_week_bags
    remaining_bags = total_bags - first_week_bags - second_week_bags
    third_week_bags = remaining_bags / 2
    fourth_week_bags = third_week_bags
    result = (third_week_bags, fourth_week_bags)
    return result

print(solution())