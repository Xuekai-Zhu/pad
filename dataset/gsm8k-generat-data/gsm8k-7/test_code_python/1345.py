def solution():
    adidas_cost = 600

    # Calculate the cost of Skechers
    sketchers_cost = adidas_cost * 5

    # Calculate the cost of Nike sneakers
    nike_cost = adidas_cost * 3

    # Calculate the total cost of all sneakers
    total_sneakers_cost = adidas_cost + sketchers_cost + nike_cost

    # Calculate the cost of clothes
    clothes_cost = 8000 - total_sneakers_cost
    result = clothes_cost
    return result

print(solution())