def solution():
    """Stephanie is checking her household budget, and needs to calculate how much she has left to pay for her bills. Her electricity bill costs $60, and this is paid in full. Her gas bill was $40, and she has already paid three-quarters of this.She makes another payment of $5 towards her gas bill while checking her budget. Her water bill is $40, which she has paid half of, and her internet bill is $25, which she has made 4 payments of $5 towards. Overall, how many dollars does Stephanie still need to pay to finish paying her bills?"""
    electricity_bill = 60
    gas_bill = 40
    gas_paid = gas_bill * 0.75 + 5
    water_bill = 40
    water_paid = water_bill * 0.5
    internet_bill = 25
    internet_paid = 4 * 5
    total_paid = electricity_bill + gas_paid + water_paid + internet_paid
    total_cost = electricity_bill + gas_bill + water_bill + internet_bill
    remaining_cost = total_cost - total_paid
    result = remaining_cost
    return result

print(solution())