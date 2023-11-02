def solution():
    # Calculate the cost of the salad and fries
    salad_price = 3 * 2  # the salad costs three times as much as one pack of fries
    fries_price = 2 * 2  # two packs of fries cost $2 each

    # Subtract the price of salad and fries from the total to get the cost of the burger
    burger_price = 15 - salad_price - fries_price
    result = burger_price
    return result

print(solution())