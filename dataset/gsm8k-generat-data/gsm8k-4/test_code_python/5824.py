def solution():
    """Barry has $10.00 worth of dimes. His little brother, Dan has half that amount but finds 2 more dimes on his way home from school. How many dimes does Dan have?"""
    # Define the value of a dime in dollars
    dime_value = 0.1

    # Calculate the total number of dimes Barry has
    barry_dimes = 10.0 / dime_value

    # Calculate the total value of dimes Dan has before finding 2 more
    dan_value = (10.0 / 2) / dime_value

    # Add the 2 extra dimes Dan found
    dan_value += 2

    # Calculate the total number of dimes Dan has
    dan_dimes = dan_value / dime_value

    # Return the result
    result = dan_dimes
    return result

print(solution())