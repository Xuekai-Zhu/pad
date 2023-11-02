def solution():
    total_bags_sold = 100
    first_week_sales = 15

    # Calculate the number of bags sold in the second week
    second_week_sales = first_week_sales * 3

    # Calculate the total number of bags sold in the first two weeks
    first_two_weeks_sales = first_week_sales + second_week_sales

    # Calculate the total number of bags sold in the last two weeks
    last_two_weeks_sales = total_bags_sold - first_two_weeks_sales

    # Since there were an equal number of chips sold in the third and fourth week, divide the total number of bags sold in the last two weeks by 2
    num_bags_per_week = last_two_weeks_sales / 2

    result = num_bags_per_week
    return result

print(solution())