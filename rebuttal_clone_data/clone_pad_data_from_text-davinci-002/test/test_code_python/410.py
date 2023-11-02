def solution():
     paintings_bought = 10
     painting_cost = 40
     toys_bought = 8
     toy_cost = 20
     painting_selling_price = painting_cost * 0.9
     toy_selling_price = toy_cost * 0.85
     total_painting_revenue = painting_selling_price * paintings_bought
     total_toy_revenue = toy_selling_price * toys_bought
     total_revenue = total_painting_revenue + total_toy_revenue
     total_cost = painting_cost * paintings_bought + toy_cost * toys_bought
     loss = total_cost - total_revenue
     result = loss
     return result

print(solution())