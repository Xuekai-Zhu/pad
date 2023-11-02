def solution():
     total_pies = 200
     total_sales = total_pies * 20
     money_for_ingredients = total_sales * (3/5)
     money_remaining = total_sales - money_for_ingredients
     result = money_remaining
    return result

print(solution())