def solution():
    # Calculate the annual cost for Juanita to buy the newspaper daily
    daily_cost = (0.5 * 6) + 2  # Monday through Saturday the cost is $0.50, and Sunday the cost is $2.00
    annual_cost_Juanita = daily_cost * 365  # 365 days in a year
    annual_cost_Grant = 200
    cost_difference = annual_cost_Juanita - annual_cost_Grant
    result = cost_difference
    return result

print(solution())