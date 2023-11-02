def solution():
    """The city is holding its annual rubber duck race for charity. The regular size rubber ducks are $3.00 each and the large size rubber duck is $5.00 each. All of the rubber ducks will be dropped into the river at the same time and the first duck that floats across the finish line wins. They sold 221 regular size ducks and 185 large size ducks. How much money did the city raise for charity?"""
    # Define the price of regular and large rubber ducks
    regular_price = 3
    large_price = 5

    # Calculate the total revenue from regular and large ducks
    regular_revenue = regular_price * 221
    large_revenue = large_price * 185

    # Calculate the total revenue raised for charity
    total_revenue = regular_revenue + large_revenue

    # return the result
    result = total_revenue
    return result

print(solution())