def solution():
     """Arven bought five puppies for a total cost of $800. Three puppies are on sale for $150 each. How much does each of those two other puppies cost if they cost the same?"""
     total_cost = 800
     sale_puppies = 3
     sale_price = 150
     cost_of_other_puppies = total_cost - (sale_puppies * sale_price)
     cost_of_each_puppy = cost_of_other_puppies / 2
     result = cost_of_each_puppy
     return result

print(solution())