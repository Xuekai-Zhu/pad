def solution():
    """The dinner bill for 6 friends came to $150. Silas said he would pay for half of the bill and the remaining friends could split the rest of the bill and leave a 10% tip for the whole meal. How many dollars will one of the friends pay?"""
    # Define the number of friends and the total bill
    num_friends = 6
    total_bill = 150

    # Calculate Silas's payment and the remaining bill
    silas_payment = total_bill / 2
    remaining_bill = total_bill - silas_payment

    # Calculate the tip for the whole meal
    tip = remaining_bill * 0.1

    # Calculate the total cost for the remaining friends including the tip
    total_cost_remaining = remaining_bill + tip

    # Calculate the cost per friend
    cost_per_friend = total_cost_remaining / (num_friends - 1)

    result = round(cost_per_friend, 2)
    return result

print(solution())