def solution():
    """Shaniqua styles hair. For every haircut she makes $12 and for every style she makes $25. How many dollars would Shaniqua make if she gave 8 haircuts and 5 styles?"""
    # Define the price for a haircut and a style
    HAIRCUT_PRICE = 12
    STYLE_PRICE = 25

    # Define the number of haircuts and styles Shaniqua gave
    haircuts = 8
    styles = 5

    # Calculate the total earnings
    earnings = (haircuts * HAIRCUT_PRICE) + (styles * STYLE_PRICE)

    # Display the total earnings
    result = earnings
    return result

print(solution())