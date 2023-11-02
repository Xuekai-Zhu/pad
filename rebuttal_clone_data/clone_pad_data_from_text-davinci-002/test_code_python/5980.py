def solution():
     dogs = 3
     puppies_per_dog = 4
     shots_per_puppy = 2
     cost_per_shot = 5
 
     total_shots = dogs * puppies_per_dog * shots_per_puppy
     total_cost = total_shots * cost_per_shot
 
     result = total_cost
 
     return result

print(solution())