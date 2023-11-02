def solution():
    pairs_of_shoes = 6  # Sab and Dane sold 6 pairs of shoes
    cost_per_shoe = 3  # Each pair of shoes cost $3
    total_cost_shoes = pairs_of_shoes * cost_per_shoe  # Calculate the total cost of selling shoes

    shirts = 18  # Sab and Dane sold 18 shirts
    cost_per_shirt = 2  # Each shirt cost $2
    total_cost_shirts = shirts * cost_per_shirt  # Calculate the total cost of selling shirts

    total_earning = total_cost_shoes + total_cost_shirts  # Calculate the total earning

    # Divide the total earning between Sab and Dane
    earnings_per_person = total_earning / 2
    result = earnings_per_person
    return result

print(solution())