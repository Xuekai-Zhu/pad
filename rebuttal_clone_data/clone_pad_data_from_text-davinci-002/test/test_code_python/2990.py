def solution():
      milk_cost = 3
      bananas_cost = 2
      sales_tax = 0.2
      total_cost = milk_cost + bananas_cost + (milk_cost + bananas_cost) * sales_tax
      result = total_cost
      return result

print(solution())