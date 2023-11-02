def solution():
    # Calculate the number of guests who responded with a Yes or No
    responded = 0.83 * 200 + 0.09 * 200  # 83% of guests responded with a Yes, 9% of guests responded with a No
    # Calculate the number of guests who did not respond
    not_responded = 200 - responded
    result = not_responded
    return result

print(solution())