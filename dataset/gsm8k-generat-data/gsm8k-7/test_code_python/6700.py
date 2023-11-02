def solution():
    max_price = 10
    options = [
        {"oz": 10, "price": 1},
        {"oz": 16, "price": 2},
        {"oz": 25, "price": 2.5},
        {"oz": 50, "price": 5},
        {"oz": 200, "price": 10}
    ]

    # Sort the ketchup options by price per ounce (cheapest first)
    options = sorted(options, key=lambda x: x["price"]/x["oz"])

    # Keep buying the cheapest option until we run out of money
    num_bottles = 0
    for option in options:
        while max_price >= option["price"]:
            max_price -= option["price"]
            num_bottles += 1

    result = num_bottles
    return result

print(solution())