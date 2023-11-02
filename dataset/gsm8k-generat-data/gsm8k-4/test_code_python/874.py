def solution():
    """Winston has 14 quarters. He then spends half a dollar on candy. How many cents does he have left?"""
    # Define the value of a quarter and half a dollar in cents
    QUARTER_VALUE = 25
    HALF_DOLLAR_VALUE = 50

    # Calculate the total value of the quarters in cents
    quarters_value = 14 * QUARTER_VALUE

    # Calculate the remaining value after spending half a dollar
    remaining_value = quarters_value - HALF_DOLLAR_VALUE

    # Convert the remaining value to cents
    remaining_cents = remaining_value % 100

    # Return the remaining cents
    result = remaining_cents
    return result

print(solution())