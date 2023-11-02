def solution():
    """Marcel goes to the store with Dale to buy groceries for cooking dinner. Marcel buys 10 ears of corn, and Dale buys half that amount. Dale buys 8 potatoes and Marcel buys some, too. If they check out together and end up buying 27 vegetables, how many potatoes did Marcel buy?"""
    # Marcel buys 10 ears of corn
    marcel_corn = 10

    # Dale buys half that amount
    dale_corn = marcel_corn / 2

    # Dale buys 8 potatoes
    dale_potatoes = 8

    # Calculate how many vegetables Marcel bought
    marcel_veg = 27 - (marcel_corn + dale_corn + dale_potatoes)

    # Divide Marcel's vegetables in half, assuming he bought an equal number of potatoes and another vegetable
    marcel_potatoes = marcel_veg / 2

    # Display how many potatoes Marcel bought
    result = marcel_potatoes
    return result

print(solution())