def solution():
    """Karen has 32 quarters in her piggy bank.  Her older brother Christopher has 64 quarters in his piggy bank.  How much more money does Christopher have?"""
    # Define the value of a quarter in cents
    QUARTER_VALUE = 25

    # Calculate the value of Karen's quarters in cents
    karen_value = 32 * QUARTER_VALUE

    # Calculate the value of Christopher's quarters in cents
    christopher_value = 64 * QUARTER_VALUE

    # Calculate the difference in value between Christopher's and Karen's quarters
    difference = christopher_value - karen_value

    # Convert the difference in value to dollars
    difference_dollars = difference / 100

    # Display the difference in dollars
    result = difference_dollars
    return result

print(solution())