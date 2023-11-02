def solution():
    """Winston has 14 quarters. He then spends half a dollar on candy. How many cents does he have left?"""
    # Define the value of a quarter in cents
    QUARTER_VALUE = 25

    # Calculate the total value of Winston's quarters in cents
    total_quarters_value = 14 * QUARTER_VALUE

    # Subtract half a dollar (50 cents) from Winston's total
    remaining_total = total_quarters_value - 50

    # Convert the remaining total to just cents
    remaining_cents = remaining_total % 100

    # Display the remaining cents
    result = remaining_cents
    return result

print(solution())