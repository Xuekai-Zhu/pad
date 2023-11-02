def solution():
     ticket_cost = 5
     popcorn_cost = ticket_cost * 0.8
     soda_cost = popcorn_cost * 0.5
     total_cost = (4 * ticket_cost) + (2 * popcorn_cost) + (4 * soda_cost)
     result = total_cost
     return result

print(solution())