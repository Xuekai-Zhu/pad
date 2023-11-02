def solution():
    # Calculate the number of chickens left with Paul to sell at the market
    total_chickens = 80  # total number of chickens Paul had to sell
    sold_to_neighbor = 12  # number of chickens sold to the neighbor before leaving the farm
    sold_before_market = 25  # number of chickens sold before the market opens 
    chickens_left = total_chickens - sold_to_neighbor - sold_before_market   # number of chickens left to sell at the market
    result = chickens_left
    return result

print(solution())