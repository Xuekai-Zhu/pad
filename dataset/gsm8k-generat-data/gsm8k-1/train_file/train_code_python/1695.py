def solution():
    """The dinner bill for 6 friends came to $150. Silas said he would pay for half of the bill and the remaining friends could split the rest of the bill and leave a 10% tip for the whole meal. How many dollars will one of the friends pay?"""
    total_friends = 6
    bill = 150
    silas_payment = bill / 2
    remaining_friends = total_friends - 1
    remaining_bill = bill - silas_payment
    bill_with_tip = remaining_bill * 1.1
    cost_per_friend = bill_with_tip / remaining_friends
    result = cost_per_friend
    return result

print(solution())