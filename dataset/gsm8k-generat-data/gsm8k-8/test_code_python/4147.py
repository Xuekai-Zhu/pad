def solution():
    # Define the number of stamps Mike gave Tom
    mike_gift = 17

    # Calculate the number of stamps Harry gave Tom
    harry_gift = 10 + 2 * mike_gift

    # Calculate the total number of stamps Tom now has
    total_stamps = 3000 + mike_gift + harry_gift

    result = total_stamps
    return result

print(solution())