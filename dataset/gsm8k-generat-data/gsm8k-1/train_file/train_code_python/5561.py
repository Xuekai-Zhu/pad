def solution():
    """Marcel goes to the store with Dale to buy groceries for cooking dinner. Marcel buys 10 ears of corn, and Dale buys half that amount. Dale buys 8 potatoes and Marcel buys some, too. If they check out together and end up buying 27 vegetables, how many potatoes did Marcel buy?"""
    marcel_corn = 10
    dale_corn = marcel_corn / 2
    dale_potatoes = 8
    total_veggies = 27
    marcel_potatoes = total_veggies - (marcel_corn + dale_corn + dale_potatoes)
    result = marcel_potatoes
    return result

print(solution())