def solution():
    num_shorts = 3
    shorts_price = 16.5

    num_pants = 3
    pants_price = 22.5

    num_shoes = 3
    shoes_price = 42

    # Calculate the total cost of all shorts
    total_shorts_cost = num_shorts * shorts_price

    # Calculate the total cost of all pants
    total_pants_cost = num_pants * pants_price

    # Calculate the total cost of all shoes
    total_shoes_cost = num_shoes * shoes_price

    # Calculate the total cost of all clothing items
    total_cost = total_shorts_cost + total_pants_cost + total_shoes_cost
    result = total_cost
    return result

print(solution())