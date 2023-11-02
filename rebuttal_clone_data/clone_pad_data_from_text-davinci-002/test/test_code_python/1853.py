def solution():
     leila_bags = 2
     leila_toys_per_bag = 25
     mohamed_bags = 3
     mohamed_toys_per_bag = 19
     leila_total_toys = leila_bags * leila_toys_per_bag
     mohamed_total_toys = mohamed_bags * mohamed_toys_per_bag
     toys_donated = mohamed_total_toys - leila_total_toys
     result = toys_donated
     return result

print(solution())