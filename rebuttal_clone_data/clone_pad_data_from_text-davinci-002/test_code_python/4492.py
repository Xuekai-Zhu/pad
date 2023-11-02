def solution():
     skirts = 2
     blouses = 3
     skirt_cost = 13
     blouse_cost = 6
     total_cost = (skirts * skirt_cost) + (blouses * blouse_cost)
     paid = 100
     change = paid - total_cost
     result = change
     return result

print(solution())