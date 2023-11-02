def solution():
    """Nina has received a scholarship worth $8000 less than Kelly's amount. Kelly received a scholarship worth twice the amount Wendy received. How much money did they receive in scholarship together if Wendy received a scholarship worth $20000?"""
    # Define the amount of scholarship Wendy received
    wendy_scholarship = 20000

    # Calculate Kelly's scholarship amount
    kelly_scholarship = wendy_scholarship * 2

    # Calculate Nina's scholarship amount
    nina_scholarship = kelly_scholarship - 8000

    # Calculate the total scholarship amount
    total_scholarship = wendy_scholarship + kelly_scholarship + nina_scholarship

    # return the result
    result = total_scholarship
    return result

print(solution())