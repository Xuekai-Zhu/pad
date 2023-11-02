def solution():
    # Calculate the total cost of the two almond and cheese croissants
    croissant_cost = 4.5
    num_croissants = 2
    total_croissant_cost = croissant_cost * num_croissants

    # Calculate the cost of the plain croissant and focaccia
    plain_croissant_cost = 3.0
    focaccia_cost = 4.0
    total_bread_cost = plain_croissant_cost + focaccia_cost

    # Calculate the cost of the two lattes
    latte_cost = 2.5
    num_lattes = 2
    total_latte_cost = latte_cost * num_lattes

    # Calculate the total cost for all items
    total_cost = total_croissant_cost + total_bread_cost + total_latte_cost

    result = total_cost
    return result

print(solution())