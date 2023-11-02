def solution():
     betty_cupcakes = 10
     dora_cupcakes = 8
     hours_worked = 5
     betty_total_cupcakes = (hours_worked - 2) * betty_cupcakes
     dora_total_cupcakes = hours_worked * dora_cupcakes
     difference = dora_total_cupcakes - betty_total_cupcakes
     result = difference
     return result

print(solution())