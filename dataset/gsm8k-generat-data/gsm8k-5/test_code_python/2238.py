def solution():
    total_chickens = 80
    sold_to_neighbor = 12
    sold_before_market = 25

    # Calculate the number of chickens left with Paul to sell at the market
    remaining_chickens = total_chickens - sold_to_neighbor - sold_before_market
    result = remaining_chickens
    return result

print(solution())