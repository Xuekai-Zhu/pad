def solution():
    """Bill is ordering a new truck. He has decided to purchase a two-ton truck with several added features: a king cab upgrade, a towing package, leather seats, running boards, and the upgraded exterior light package. The base price of the truck is $30,000, and the other features are at extra cost. The king cab is an extra $7,500, leather seats are one-third the cost of the king cab upgrade, running boards are $500 less than the leather seats, and the upgraded exterior light package is $1500. What is the total cost of Bill's new truck, in dollars?"""
    base_price = 30000
    king_cab_price = 7500
    leather_seats_price = king_cab_price / 3
    running_boards_price = leather_seats_price - 500
    light_package_price = 1500
    total_price = base_price + king_cab_price + leather_seats_price + running_boards_price + light_package_price
    result = total_price
    return result

print(solution())