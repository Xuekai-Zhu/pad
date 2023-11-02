def solution():
    """The city is holding its annual rubber duck race for charity. The regular size rubber ducks are $3.00 each and the large size rubber duck is $5.00 each. All of the rubber ducks will be dropped into the river at the same time and the first duck that floats across the finish line wins. They sold 221 regular size ducks and 185 large size ducks. How much money did the city raise for charity?"""
    regular_price = 3
    large_price = 5
    regular_count = 221
    large_count = 185
    total_regular_price = regular_price * regular_count
    total_large_price = large_price * large_count
    total_price = total_regular_price + total_large_price
    result = total_price
    return result

print(solution())