def solution():
    total_cost = 800
    num_sale_puppies = 3
    sale_price = 150

    # Calculate the total cost of the three puppies on sale
    sale_cost = num_sale_puppies * sale_price

    # Calculate the total cost of the two other puppies
    other_cost = total_cost - sale_cost

    # Calculate the cost of each of the two other puppies
    cost_per_puppy = other_cost / 2
    result = cost_per_puppy
    return result

print(solution())