def solution():
    # Calculate the cost of pool cleaning per month
    clean_cost = 150 * 30/3  # $150 per cleaning, done every 3 days, so 10 cleanings in a month
    tip = clean_cost * 0.10  # 10% tip on the cleaning cost
    chemicals_cost = 200 * 2  # $200 spent on chemicals twice a month
    total_cost = clean_cost + tip + chemicals_cost
    result = total_cost
    return result

print(solution())