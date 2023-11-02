def solution():
    house_price = 100000  # Roger bought a house for $100,000
    down_payment = 0.2  # Roger paid 20% down
    remaining_balance = house_price * (1 - down_payment)  # Calculate the remaining balance
    parents_payment = 0.3 * remaining_balance  # Roger's parents paid off 30% of the remaining balance

    # Calculate the final amount Roger still owes on his house
    total_remaining_balance = remaining_balance - parents_payment
    result = total_remaining_balance
    return result

print(solution())