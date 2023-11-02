def solution():
     total_eggs = 30
     fertile_eggs = 0.8 * total_eggs
     non_fertile_eggs = 0.2 * total_eggs
     calcified_eggs = 0.3 * fertile_eggs
     hatched_eggs = fertile_eggs - calcified_eggs
     result = hatched_eggs
     return result

print(solution())