def solution():
     total_melons_sold = 46
     one_melon_customers = 17
     three_melon_customers = 3
     two_melon_customers = total_melons_sold - one_melon_customers - three_melon_customers
     result = two_melon_customers
     return result

print(solution())