def solution():
    pieces_per_pizza = 8  # There are 8 pieces in a pizza
    pieces_per_day = 3  # Nunzio eats 3 pieces of pizza every day
    days = 72  # Nunzio wants to know how many pizzas he will eat in 72 days

    # Calculate the total number of pieces Nunzio will eat in 72 days
    total_pieces = pieces_per_day * days

    # Convert the total number of pieces to number of pizzas
    total_pizzas = total_pieces / pieces_per_pizza
    result = total_pizzas
    return result

print(solution())