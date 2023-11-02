def solution():
    """Stephanie is checking her household budget, and needs to calculate how much she has left to pay for her bills. Her electricity bill costs $60, and this is paid in full. Her gas bill was $40, and she has already paid three-quarters of this. She makes another payment of $5 towards her gas bill while checking her budget. Her water bill is $40, which she has paid half of, and her internet bill is $25, which she has made 4 payments of $5 towards. Overall, how many dollars does Stephanie still need to pay to finish paying her bills?"""
    # Define the costs of each bill and the payments made
    electricity_cost = 60
    gas_cost = 40
    gas_payments = 3 * gas_cost / 4 + 5
    water_cost = 40
    water_payments = water_cost / 2
    internet_cost = 25
    internet_payments = 4 * 5

    # Calculate the total cost and payments
    total_cost = electricity_cost + gas_cost + water_cost + internet_cost
    total_payments = gas_payments + water_payments + internet_payments

    # Calculate the remaining amount to be paid
    remaining_cost = total_cost - total_payments

    # return the result
    result = remaining_cost
    return result

print(solution())