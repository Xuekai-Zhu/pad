def solution():
    num_skirts = 3
    skirt_price = 20.0

    num_pants = 2
    pants_price = 30.0

    num_blouses = 5
    blouse_price = 15.0

    # Calculate the total cost of all skirts
    total_skirt_cost = num_skirts * skirt_price

    # Calculate the total cost of all blouses
    total_blouse_cost = num_blouses * blouse_price

    # Calculate the cost of both pairs of pants
    pants_cost = 2 * pants_price

    # Calculate the cost of the discounted pair of pants
    discounted_pants_cost = 0.5 * pants_price

    # Calculate the total cost of all pants
    total_pants_cost = pants_cost - discounted_pants_cost

    # Calculate the total cost of all clothing items
    total_cost = total_skirt_cost + total_pants_cost + total_blouse_cost
    result = total_cost
    return result

print(solution())