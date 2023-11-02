def solution():
     selling_price = 30
     pairs_sold = 10
     sign_cost = 20
     total_sales = selling_price * pairs_sold
     total_expenses = total_sales / 2 + sign_cost
     per_pair_cost = total_expenses / pairs_sold
     result = per_pair_cost
     return result

print(solution())