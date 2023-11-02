def solution():
    """The city is holding its annual rubber duck race for charity. The regular size rubber ducks are $3.00 each and the large size rubber duck is $5.00 each. All of the rubber ducks will be dropped into the river at the same time and the first duck that floats across the finish line wins. They sold 221 regular size ducks and 185 large size ducks. How much money did the city raise for charity?"""
    regular_duck_cost = 3
    large_duck_cost = 5
    regular_ducks_sold = 221
    large_ducks_sold = 185
    total_money_raised = (regular_duck_cost * regular_ducks_sold) + (large_duck_cost * large_ducks_sold)
    result = total_money_raised
    return result

print(solution())