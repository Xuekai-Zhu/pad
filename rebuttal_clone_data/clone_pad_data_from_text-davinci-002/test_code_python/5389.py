def solution():
     Claw_per_foot = 4
     Nails_time = 10
     Ears_time = 90
     Shampoo_time = 300
     Grooming_time = (Nails_time * Claw_per_foot) + Ears_time + Shampoo_time
     result = Grooming_time
     return result

print(solution())