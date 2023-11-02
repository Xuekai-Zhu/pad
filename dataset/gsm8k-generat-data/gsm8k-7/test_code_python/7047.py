def solution():
    num_jackets = 3
    jacket_price = 10

    num_shorts = 2
    shorts_price = 6

    num_pants = 4
    pants_price = 12

    # Calculate the total cost of all jackets
    total_jacket_cost = num_jackets * jacket_price

    # Calculate the total cost of all shorts
    total_shorts_cost = num_shorts * shorts_price

    # Calculate the total cost of all pants
    total_pants_cost = num_pants * pants_price

    # Calculate the total cost of all clothing items
    total_cost = total_jacket_cost + total_shorts_cost + total_pants_cost
    result = total_cost
    return result

print(solution())