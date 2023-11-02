def solution():
    # Define the amount of maize stored each month
    maize_per_month = 1

    # Calculate the total amount of maize stored over 2 years
    total_maize = maize_per_month * 12 * 2

    # Adjust for stolen and donated maize
    total_maize = total_maize - 5 + 8

    result = total_maize
    return result

print(solution())