def solution():
    """Kylie picks apples for 3 hours. The first hour she picks 66 apples. The second hour she doubles her apple picking rate, and the third hour she picks a third of the apples picked in the first hour. How many apples did Kylie pick total?"""
    # Define the number of apples picked in the first hour
    apples_1 = 66

    # Calculate the number of apples picked in the second hour
    apples_2 = apples_1 * 2

    # Calculate the number of apples picked in the third hour
    apples_3 = apples_1 / 3

    # Calculate the total number of apples picked
    total_apples = apples_1 + apples_2 + apples_3

    # Display the total number of apples picked
    result = total_apples
    return result

print(solution())