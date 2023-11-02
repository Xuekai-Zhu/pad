def solution():
   geckos = 3
   iguanas = 2
   snakes = 4
   monthly_gecko_cost = 15
   monthly_iguana_cost = 5
   monthly_snake_cost = 10
   total_monthly_cost = (geckos * monthly_gecko_cost) + (iguanas * monthly_iguana_cost) + (snakes * monthly_snake_cost)
   total_yearly_cost = total_monthly_cost * 12
   result = total_yearly_cost
   return result

print(solution())