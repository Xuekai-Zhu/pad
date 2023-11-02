def solution():
    # Define the costs of each CD
    the_life_journey = 100
    a_day_a_life = 50
    when_you_rescind = 85

    # Calculate the total cost of buying 3 of each CD
    total_cost = 3 * (the_life_journey + a_day_a_life + when_you_rescind)

    result = total_cost
    return result

print(solution())