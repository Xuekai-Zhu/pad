def solution():
     total_eggs = 3 * 12
     eggs_used_crepes = total_eggs / 4
     eggs_left_1 = total_eggs - eggs_used_crepes
     eggs_used_cupcakes = eggs_left_1 * 2 / 3
     eggs_left_2 = eggs_left_1 - eggs_used_cupcakes
     result = eggs_left_2
     
     return result

print(solution())