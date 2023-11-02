def solution():
    """James finds 3 bills in his pocket. They are all 20s. If he already had $75 in his wallet how much money does he have now?"""
    # Define the value of each bill
    bill_value = 20

    # Define the number of bills found in James' pocket
    num_bills = 3

    # Calculate the total value of the bills found in James' pocket
    pocket_money = bill_value * num_bills

    # Add the pocket money to James' wallet balance
    total_money = pocket_money + 75

    result = total_money
    return result

print(solution())