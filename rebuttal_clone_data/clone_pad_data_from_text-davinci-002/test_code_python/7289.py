def solution():
     hot_dog_cost = 1.50
     salad_cost = 2.50
     total_cost = hot_dog_cost * 5 + salad_cost * 3
     payment = 10 + 10
     change = payment - total_cost
     result = change
     return result

print(solution())