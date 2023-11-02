def solution():
    num_shirts = 4  # Carrie buys 4 shirts
    num_pants = 2  # Carrie buys 2 pairs of pants
    num_jackets = 2  # Carrie buys 2 jackets
    cost_per_shirt = 8  # Each shirt costs $8
    cost_per_pant = 18  # Each pair of pants costs $18
    cost_per_jacket = 60  # Each jacket costs $60

    # Calculate the total cost of all the clothes
    total_cost = (num_shirts * cost_per_shirt) + (num_pants * cost_per_pant) + (num_jackets * cost_per_jacket)

    # Calculate the amount Carrie needs to pay (half of total cost)
    carrie_payment = total_cost / 2
    result = carrie_payment
    return result

print(solution())