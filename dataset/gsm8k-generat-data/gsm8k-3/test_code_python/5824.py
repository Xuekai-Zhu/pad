def solution():
    """Barry has $10.00 worth of dimes.  His little brother, Dan has half that amount but finds 2 more dimes on his way home from school.  How many dimes does Dan have?"""
    # Define the value of a dime in dollars
    DIME_VALUE = 0.1

    # Calculate the number of dimes Barry has based on the value
    barry_dimes = int(10 // DIME_VALUE)

    # Calculate the total value of Dan's dimes (half of Barry's value plus 0.2 for the extra two dimes)
    dan_value = (10/2 + 0.2)

    # Calculate the number of dimes Dan has based on the value
    dan_dimes = int(dan_value // DIME_VALUE)

    # Display the number of dimes Dan has
    result = dan_dimes
    return result

print(solution())