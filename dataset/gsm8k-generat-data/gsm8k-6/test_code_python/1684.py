def solution():
    total_bags = 100  # total number of bags sold in a month
    first_week_sales = 15  # number of bags sold in the first week
    second_week_sales = 3 * first_week_sales  # number of bags sold in the second week is thrice the first week sales
    remaining_bags = total_bags - (first_week_sales + second_week_sales)  # number of bags remaining after the first two weeks
    third_week_sales = remaining_bags // 2  # equal number of chips sold in the third and fourth week
    fourth_week_sales = third_week_sales  # equal number of chips sold in the third and fourth week
    result = (third_week_sales, fourth_week_sales)
    return result

print(solution())