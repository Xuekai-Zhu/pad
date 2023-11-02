def solution():
    num_lollipops = 5
    lollipop_price = 0.4

    num_candies = 4
    candy_price = 3.20

    # Calculate the total cost of all lollipops
    total_lollipop_cost = num_lollipops * lollipop_price

    # Calculate the total cost of all candies
    total_candy_cost = num_candies * candy_price

    # Calculate the total cost of all items
    total_cost = total_lollipop_cost + total_candy_cost
    result = total_cost
    return result

print(solution())