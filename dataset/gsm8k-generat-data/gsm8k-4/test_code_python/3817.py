def solution():
    """Every year, Mabel gets as many quarters as she is years old. She always puts these and nothing else in a piggy bank. When she turns 7, how much money is in the bank?"""
    # Define the number of years Mabel has been getting quarters
    years = 7

    # Calculate the total number of quarters she has
    total_quarters = 0
    for i in range(1, years+1):
        total_quarters += i

    # Calculate the total amount of money in dollars
    total_dollars = total_quarters * 0.25

    # return the result
    result = total_dollars
    return result

print(solution())