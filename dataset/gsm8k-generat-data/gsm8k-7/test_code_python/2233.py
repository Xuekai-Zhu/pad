def solution():
    num_croissants = 7
    num_cakes = 18
    num_pizzas = 30

    # Calculate the total number of croissants, cakes, and pizzas consumed by Jorge and Giuliana
    total_food = num_croissants + num_cakes + num_pizzas

    # Multiply total_food by 2 to account for both Jorge and Giuliana
    total_consumed = total_food * 2
    result = total_consumed
    return result

print(solution())