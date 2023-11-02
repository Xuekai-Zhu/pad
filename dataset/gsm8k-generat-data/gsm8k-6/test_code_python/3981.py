def solution():
    # Calculate the total number of items sold by James
    first_day_sales = 20 * 2  # James sells two things at each of the 20 houses he visits on the first day
    second_day_visits = 2 * 20  # James visits twice as many houses on the second day, i.e. 40 houses
    second_day_sales = 0.8 * 40 * 2  # James sells to 80% of the 40 houses he visits on the second day, selling two things at each house
    total_sales = first_day_sales + second_day_sales
    result = total_sales
    return result

print(solution())