def solution():
    # Define the cost per piece of string cheese and the number of string cheeses per pack
    cost_per_piece = 0.10
    cheeses_per_pack = 20

    # Calculate the total cost for 3 packs of string cheese
    total_cheeses = 3 * cheeses_per_pack
    total_cost = total_cheeses * cost_per_piece

    # Convert the total cost to dollars and round to two decimal places
    dollars_paid = round(total_cost, 2)
    result = dollars_paid
    return result

print(solution())