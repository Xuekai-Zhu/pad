def solution():
    """Archibald eats 1 apple a day for two weeks. Over the next three weeks, he eats the same number of apples as the total of the first two weeks. Over the next two weeks, he eats 3 apples a day. Over these 7 weeks, how many apples does he average a week?"""
    # Define the number of apples Archibald eats in the first two weeks
    apples_first_two_weeks = 14

    # Define the number of apples Archibald eats in the next three weeks
    apples_next_three_weeks = apples_first_two_weeks

    # Define the number of apples Archibald eats in the next two weeks
    apples_next_two_weeks = 3 * 14

    # Define the total number of weeks
    total_weeks = 7

    # Calculate the total number of apples Archibald eats over 7 weeks
    total_apples = apples_first_two_weeks + apples_next_three_weeks + apples_next_two_weeks

    # Calculate the average number of apples Archibald eats per week over 7 weeks
    avg_apples_per_week = total_apples / total_weeks

    # return the result
    result = avg_apples_per_week
    return result

print(solution())