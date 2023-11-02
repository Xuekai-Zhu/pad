def solution():
    # Calculate the total number of sandwiches Paul eats in 6 days
    sandwiches_first_day = 2
    sandwiches_second_day = 2 * 2
    sandwiches_third_day = 2 * 2 * 2
    sandwiches_fourth_day = 2 * 2 * 2 * 2
    sandwiches_fifth_day = 2 * 2 * 2 * 2 * 2
    sandwiches_sixth_day = 2 * 2 * 2 * 2 * 2 * 2
    total_sandwiches = sandwiches_first_day + sandwiches_second_day + sandwiches_third_day + sandwiches_fourth_day + sandwiches_fifth_day + sandwiches_sixth_day
    result = total_sandwiches
    return result

print(solution())