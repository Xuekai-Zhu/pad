def solution():
    """Donny has $78 in his piggy bank. If Donny buys a kite for $8 and a frisbee for $9. How much money does Donny have left?"""
    # Define Donny's initial savings
    savings = 78

    # Subtract the cost of the kite and the frisbee from Donny's savings
    cost = 8 + 9
    remaining_savings = savings - cost

    # return the result
    result = remaining_savings
    return result

print(solution())