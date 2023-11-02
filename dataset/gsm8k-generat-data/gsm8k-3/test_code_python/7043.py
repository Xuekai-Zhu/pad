def solution():
    """Stephanie is checking her household budget, and needs to calculate how much she has left to pay for her bills. Her electricity bill costs $60, and this is paid in full. Her gas bill was $40, and she has already paid three-quarters of this. She makes another payment of $5 towards her gas bill while checking her budget. Her water bill is $40, which she has paid half of, and her internet bill is $25, which she has made 4 payments of $5 towards. Overall, how many dollars does Stephanie still need to pay to finish paying her bills?"""
    # Calculate the amount still owed on the gas bill
    gas_cost = 40
    gas_paid = gas_cost * 0.75 + 5
    gas_owed = gas_cost - gas_paid

    # Calculate the amount still owed on the water bill
    water_cost = 40
    water_paid = water_cost * 0.5
    water_owed = water_cost - water_paid

    # Calculate the amount still owed on the internet bill
    internet_cost = 25
    internet_paid = 4 * 5
    internet_owed = internet_cost - internet_paid

    # Calculate the total amount still owed
    total_owed = gas_owed + water_owed + internet_owed

    # Display the total amount still owed
    result = total_owed
    return result

print(solution())