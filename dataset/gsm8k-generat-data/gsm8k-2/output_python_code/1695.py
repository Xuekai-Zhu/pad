def solution():
    """The dinner bill for 6 friends came to $150. Silas said he would pay for half of the bill and the remaining friends could split the rest of the bill and leave a 10% tip for the whole meal. How many dollars will one of the friends pay?"""
    total_bill = 150
    silas_contribution = total_bill / 2
    remaining_friends = 6 - 1 # Silas is contributing
    bill_share = (total_bill - silas_contribution) * 1.1 / remaining_friends
    result = bill_share
    return result

print(solution())