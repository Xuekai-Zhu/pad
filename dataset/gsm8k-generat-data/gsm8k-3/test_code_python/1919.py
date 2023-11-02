def solution():
    """Roger bought a house for $100,000.  He was able to pay 20% down, and his parents paid off an additional 30% of the remaining balance.  How much money does Roger still owe on his house?"""
    # Define the cost of the house and the down payment percentage
    COST = 100000
    DOWN_PAYMENT_PERCENTAGE = 0.2

    # Calculate the down payment
    down_payment = COST * DOWN_PAYMENT_PERCENTAGE

    # Calculate the remaining balance after the down payment
    remaining_balance = COST - down_payment

    # Calculate the amount paid off by Roger's parents
    parent_payment = remaining_balance * 0.3

    # Calculate the final remaining balance
    final_balance = remaining_balance - parent_payment

    # Display the final remaining balance
    result = final_balance
    return result

print(solution())