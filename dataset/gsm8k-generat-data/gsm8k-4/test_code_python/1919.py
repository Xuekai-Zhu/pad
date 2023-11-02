def solution():
    """Roger bought a house for $100,000. He was able to pay 20% down, and his parents paid off an additional 30% of the remaining balance. How much money does Roger still owe on his house?"""
    # Define the initial cost of the house and the down payment
    house_cost = 100000
    down_payment = house_cost * 0.2

    # Calculate the remaining balance after the down payment
    remaining_balance = house_cost - down_payment

    # Calculate the amount paid by Roger's parents
    parents_payment = remaining_balance * 0.3

    # Calculate the total amount owed by Roger
    total_owed = remaining_balance - parents_payment

    result = total_owed
    return result

print(solution())