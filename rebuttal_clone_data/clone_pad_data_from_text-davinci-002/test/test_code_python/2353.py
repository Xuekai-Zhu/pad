def solution():
     num_blocks = 1
     for i in range(1, 4):
         num_blocks = num_blocks + 3**i
     result = num_blocks
     return result

print(solution())