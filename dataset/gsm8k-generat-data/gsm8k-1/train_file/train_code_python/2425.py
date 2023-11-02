def solution():
    """Nina has received a scholarship worth $8000 less than Kelly's amount.
    Kelly received a scholarship worth twice the amount Wendy received.
    How much money did they receive in scholarship together if Wendy received a scholarship worth $20000?"""
    wendy_amount = 20000
    kelly_amount = 2 * wendy_amount
    nina_amount = kelly_amount - 8000
    total_amount = wendy_amount + kelly_amount + nina_amount
    result = total_amount
    return result

print(solution())