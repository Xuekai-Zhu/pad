def solution():
    # Calculate the cost of Nike and Skechers sneakers
    adidas_cost = 600
    nike_cost = 3 * adidas_cost
    skechers_cost = 5 * adidas_cost

    # Calculate the total cost of athletic sneakers
    total_sneakers_cost = adidas_cost + nike_cost + skechers_cost

    # Calculate the amount spent on clothes
    clothes_cost = 8000 - total_sneakers_cost
    result = clothes_cost
    return result

print(solution())