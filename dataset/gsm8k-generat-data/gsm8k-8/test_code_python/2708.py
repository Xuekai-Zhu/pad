def solution():
    # Define the initial savings and the number of months passed
    savings = 10
    months_passed = 5 - 1  # Counting from January to May, 4 months have passed

    # Calculate the amount of savings in May
    for i in range(months_passed):
        savings *= 2

    result = savings
    return result

print(solution())