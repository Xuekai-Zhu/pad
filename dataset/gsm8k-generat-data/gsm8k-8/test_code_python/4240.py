def solution():
    # Let's denote Diane's age when she turns 30 as x
    x = 30

    # We know that Diane is currently 16
    diane_age_now = 16

    # From the first part of the problem, we know that when Diane turns 30, she will be half the age of Alex
    alex_age_at_30 = 2 * x
    diane_age_at_30 = x
    alex_age_now = alex_age_at_30 - (x - diane_age_now)

    # From the second part of the problem, we know that when Diane turns 30, she will be twice as old as Allison
    allison_age_at_30 = x / 2
    allison_age_now = allison_age_at_30 - (x - diane_age_now)

    # Finally, we can calculate the sum of Alex and Allison's ages now
    sum_of_alex_and_allison = alex_age_now + allison_age_now
    result = sum_of_alex_and_allison
    return result

print(solution())