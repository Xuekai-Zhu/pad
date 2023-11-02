def solution():
    budget = 200  # Alexis had a budget of $200
    shirt_cost = 30
    pants_cost = 46
    coat_cost = 38
    socks_cost = 11
    belt_cost = 18

    # Calculate the total cost of the clothes
    total_clothes_cost = shirt_cost + pants_cost + coat_cost + socks_cost + belt_cost

    # Calculate how much Alexis spent on the shoes
    shoes_cost = budget - total_clothes_cost - 16  # Subtract the total clothes cost and the remaining budget

    result = shoes_cost
    return result

print(solution())