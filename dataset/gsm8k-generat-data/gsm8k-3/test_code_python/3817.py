def solution():
    """Every year, Mabel gets as many quarters as she is years old. She always puts these and nothing else in a piggy bank. When she turns 7, how much money is in the bank?"""
    # Define the value of a quarter
    QUARTER_VALUE = 0.25

    # Calculate the number of quarters Mabel gets when she is 7 years old
    num_quarters = 7

    # Calculate the total amount of money in the piggy bank
    total_money = num_quarters * QUARTER_VALUE

    # Display the total amount of money
    result = total_money
    return result

print(solution())