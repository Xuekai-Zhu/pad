def solution():
    """Marcel goes to the store with Dale to buy groceries for cooking dinner. Marcel buys 10 ears of corn, and Dale buys half that amount. Dale buys 8 potatoes and Marcel buys some, too. If they check out together and end up buying 27 vegetables, how many potatoes did Marcel buy?"""
    # Define the number of ears of corn Marcel bought
    marcel_corn = 10

    # Define the number of ears of corn Dale bought
    dale_corn = marcel_corn / 2

    # Define the number of potatoes Dale bought
    dale_potatoes = 8

    # Calculate the total number of potatoes bought
    total_potatoes = dale_potatoes + marcel_potatoes

    # Calculate the number of vegetables Marcel bought
    marcel_vegetables = 10 + marcel_potatoes

    # Calculate the number of vegetables Dale bought
    dale_vegetables = dale_corn + dale_potatoes

    # Calculate the total number of vegetables bought
    total_vegetables = marcel_vegetables + dale_vegetables

    # Calculate the number of potatoes Marcel bought
    marcel_potatoes = total_potatoes - dale_potatoes

    # Return the result
    result = marcel_potatoes
    return result

print(solution())