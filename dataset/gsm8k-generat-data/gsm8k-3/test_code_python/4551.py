def solution():
    """Maria's birthday is in 22 days. Her friend Lilly wants to buy her flowers so she saves $2 each day until Maria's birthday. If a flower costs $4, how many flowers can she buy?"""
    # Define the number of days until Maria's birthday
    days_until_birthday = 22

    # Define the amount saved each day
    savings_per_day = 2

    # Calculate the total savings
    total_savings = days_until_birthday * savings_per_day

    # Define the cost of a flower
    flower_cost = 4

    # Calculate the number of flowers Lilly can buy
    num_flowers = total_savings // flower_cost

    # Display the number of flowers
    result = num_flowers
    return result

print(solution())