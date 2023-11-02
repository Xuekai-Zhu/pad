def solution():
     shirt_cost = 7
     pair_of_shoes = shirt_cost + 3
     total_cost = (shirt_cost * 2) + pair_of_shoes
     bag_cost = total_cost / 2
     result = total_cost + bag_cost
     return result

print(solution())