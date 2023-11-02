def solution():
    """Sofia went to the department store to buy a pair of shoes and 2 shirts. A shirt costs $7 while a pair of shoes is $3 more than the shirt. If she decides to buy a bag which costs half the total price of the 2 shirts and a pair of shoes, how much will she pay for all those items?"""
    # Define the prices of the items
    shirt_price = 7
    shoes_price = shirt_price + 3

    # Calculate the cost of two shirts and a pair of shoes
    total_cost = (2 * shirt_price) + shoes_price

    # Calculate the price of the bag
    bag_price = (total_cost / 2)

    # Calculate the total cost of all items
    total_price = total_cost + bag_price

    # return the result
    result = total_price
    return result

print(solution())