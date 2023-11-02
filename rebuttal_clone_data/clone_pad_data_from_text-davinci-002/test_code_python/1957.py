def solution():
    cost_per_newspaper = 2
    percent_discount = 75
    newspapers_purchased = 500
    cost = cost_per_newspaper * (percent_discount / 100) * newspapers_purchased
    percent_sold = 80
    newspapers_sold = newspapers_purchased * (percent_sold / 100)
    profit = cost_per_newspaper * newspapers_sold - cost
    result = profit
    
    return result

print(solution())