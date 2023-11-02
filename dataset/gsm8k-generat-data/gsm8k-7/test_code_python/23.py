def solution():
    num_shorts = 5
    shorts_price = 7

    num_shoes = 2
    shoes_price = 10

    total_paid = 75

    # Calculate the total cost of the shorts
    total_shorts_cost = num_shorts * shorts_price

    # Calculate the total cost of the shoes
    total_shoes_cost = num_shoes * shoes_price

    # Calculate the total cost of all items except tops
    total_without_tops = total_shorts_cost + total_shoes_cost

    # Calculate the cost of each top
    num_tops = 4
    top_price = (total_paid - total_without_tops) / num_tops

    result = top_price
    return result

print(solution())