def solution():
    total_bowls = 70
    bowls_per_10 = 2
    num_customers = 20
    bowls_bought_per_customer = 20

    # Calculate the total number of bowls bought by all customers
    total_bowls_bought = (num_customers / 2) * bowls_bought_per_customer

    # Calculate the total number of rewards bowls given out
    total_rewards_bowls = (total_bowls_bought // 10) * bowls_per_10

    # Calculate the number of remaining rewards bowls
    remaining_rewards_bowls = total_bowls - total_rewards_bowls
    result = remaining_rewards_bowls
    return result

print(solution())