def solution():
    # Define the flat rate and the total amount paid
    flat_rate = 20
    total_amount = 146

    # Calculate the amount paid for the minutes of tutoring
    minutes_amount = total_amount - flat_rate

    # Calculate the number of minutes of tutoring
    minutes_tutored = minutes_amount / 7
    result = minutes_tutored
    return result

print(solution())