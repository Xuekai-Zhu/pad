def solution():
     cost_per_bag = 2500
     ounces_per_bag = 40
     cost_per_ounce = cost_per_bag / ounces_per_bag
     servings_per_bag = ounces_per_bag / 1
     cost_per_serving = cost_per_ounce * 1
     coupon_amount = 500
     new_cost_per_bag = cost_per_bag - coupon_amount
     new_cost_per_serving = new_cost_per_bag / servings_per_bag
     result = new_cost_per_serving
 
     return result

print(solution())