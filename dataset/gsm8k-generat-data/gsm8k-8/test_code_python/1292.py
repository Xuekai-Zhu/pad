def solution():
    # Calculate the number of fireworks needed to display the year
    fireworks_year = 4 * 6

    # Calculate the number of fireworks needed to display the message
    fireworks_message = 12 * 5

    # Calculate the total number of fireworks used, including the extra 50 boxes
    fireworks_total = (fireworks_year + fireworks_message + 50 * 8)

    result = fireworks_total
    return result

print(solution())