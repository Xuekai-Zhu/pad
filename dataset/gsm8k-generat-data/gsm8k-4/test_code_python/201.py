def solution():
    """Archibald eats 1 apple a day for two weeks. Over the next three weeks, he eats the same number of apples as the total of the first two weeks. Over the next two weeks, he eats 3 apples a day. Over these 7 weeks, how many apples does he average a week?"""
    # Define the number of apples Archibald eats each week
    apples_week1 = 1 * 7
    apples_week2 = apples_week1

    # Calculate the total number of apples Archibald eats in the first five weeks
    total_apples_5weeks = apples_week1 * 2 + apples_week2 * 3

    # Calculate the number of apples Archibald eats in the last two weeks
    apples_week6 = 3 * 7
    apples_week7 = 3 * 7

    # Calculate the total number of apples Archibald eats in all 7 weeks
    total_apples_7weeks = total_apples_5weeks + apples_week6 + apples_week7

    # Calculate the average number of apples Archibald eats per week
    average_apples = total_apples_7weeks / 7

    result = round(average_apples, 1)
    return result

print(solution())