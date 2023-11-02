def solution():
    """Nina has received a scholarship worth $8000 less than Kelly's amount.
    Kelly received a scholarship worth twice the amount Wendy received.
    How much money did they receive in scholarship together if Wendy received a scholarship worth $20000?"""
    wendy_scholarship = 20000
    kelly_scholarship = 2 * wendy_scholarship
    nina_scholarship = kelly_scholarship - 8000
    total_scholarship = wendy_scholarship + kelly_scholarship + nina_scholarship
    result = total_scholarship
    return result

print(solution())