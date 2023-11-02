def solution():
    """Sofia went to the department store to buy a pair of shoes and 2 shirts. A shirt costs $7 while a pair of shoes is $3 more than the shirt. If she decides to buy a bag which costs half the total price of the 2 shirts and a pair of shoes, how much will she pay for all those items?"""
    num_shirts = 2
    shirt_price = 7
    shoe_price = shirt_price + 3
    bag_price = ((2 * shirt_price) + shoe_price)/2
    total_price = (num_shirts * shirt_price) + shoe_price + bag_price
    result = total_price
    return result

print(solution())