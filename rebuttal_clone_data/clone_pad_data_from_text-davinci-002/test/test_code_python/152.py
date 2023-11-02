def solution():
     
     total_cost = 800
     sale_puppies = 3
     sale_price = 150
     cost_of_other_puppies = total_cost - (sale_puppies * sale_price)
     cost_of_each_puppy = cost_of_other_puppies / 2
     result = cost_of_each_puppy
     return result

print(solution())