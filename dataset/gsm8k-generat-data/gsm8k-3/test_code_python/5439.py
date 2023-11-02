def solution():
    """The city is holding its annual rubber duck race for charity.  The regular size rubber ducks are $3.00 each and the large size rubber duck is $5.00 each.  All of the rubber ducks will be dropped into the river at the same time and the first duck that floats across the finish line wins.  They sold 221 regular size ducks and 185 large size ducks.  How much money did the city raise for charity?"""
    # Define the price of a regular size rubber duck and a large size rubber duck
    REGULAR_PRICE = 3
    LARGE_PRICE = 5

    # Define the number of regular size rubber ducks and large size rubber ducks sold
    regular_ducks = 221
    large_ducks = 185

    # Calculate the total money raised for charity
    total_money = (regular_ducks * REGULAR_PRICE) + (large_ducks * LARGE_PRICE)

    # Display the total money raised for charity
    result = total_money
    return result

print(solution())