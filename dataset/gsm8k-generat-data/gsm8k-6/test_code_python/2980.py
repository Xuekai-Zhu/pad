def solution():
    total_customers = 20
    bowls_per_customer = 2/10 * 10  # Howard rewards 2 bowls for every 10 bought
    total_rewards_bowls_given = bowls_per_customer * total_customers  # total reward bowls given
    total_bought_bowls = 20 * 10 / 2  # half of the customers bought 20 bowls each
    remaining_bowls = 70 - total_rewards_bowls_given - total_bought_bowls  # calculate the remaining bowls
    result = remaining_bowls
    return result

print(solution())