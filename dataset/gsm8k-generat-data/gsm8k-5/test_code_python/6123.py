def solution():
    red_price = 20000  # Price of a single red tractor
    red_commission = 0.1  # Commission rate for selling a red tractor
    green_commission = 0.2  # Commission rate for selling a green tractor
    red_sales = 2  # Number of red tractors sold
    green_sales = 3  # Number of green tractors sold
    total_sales = red_sales * red_price + green_sales * green_price  # Total sales made by Tobias

    # Solve the equation to find the price of a single green tractor
    green_price = (7000 - red_sales * red_commission * red_price) / (green_sales * green_commission)

    result = green_price
    return result

print(solution())