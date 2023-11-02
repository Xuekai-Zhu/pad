def solution():
    """Shaniqua styles hair. For every haircut she makes $12 and for every style she makes $25. How many dollars would Shaniqua make if she gave 8 haircuts and 5 styles?"""
    # Define the prices for a haircut and a style
    HAIRCUT_PRICE = 12
    STYLE_PRICE = 25

    # Define the number of haircuts and styles Shaniqua made
    haircuts = 8
    styles = 5

    # Calculate the total amount of money Shaniqua made
    total_money = (haircuts * HAIRCUT_PRICE) + (styles * STYLE_PRICE)

    # return the result
    result = total_money
    return result

print(solution())