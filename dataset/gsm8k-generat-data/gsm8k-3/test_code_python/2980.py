def solution():
    """At his craftwork store, Howard has a collection of 70 wooden bowls where he rewards two to his customers for every 10 they buy. If he had 20 customers that day, half of whom bought 20 bowls each, calculate the number of bowls remaining in the rewards collection."""
    # Define the number of bowls given as reward for every 10 bought
    REWARD_PER_10 = 2

    # Define the initial number of wooden bowls
    initial_bowls = 70

    # Define the number of customers and the bowls bought by each customer
    num_customers = 20
    bowls_per_customer = [20 if i < num_customers/2 else 0 for i in range(num_customers)]

    # Calculate the total number of bowls bought
    total_bowls_bought = sum(bowls_per_customer)

    # Calculate the number of rewards to be given
    num_rewards = total_bowls_bought // 10 * REWARD_PER_10

    # Calculate the remaining number of wooden bowls
    remaining_bowls = initial_bowls - num_rewards

    # Display the remaining number of wooden bowls
    result = remaining_bowls
    return result

print(solution())