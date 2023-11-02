def solution():
     blocks = 9
     blocks_used = blocks
     for i in range(1, 5):
         blocks = blocks - 2
         blocks_used = blocks_used + blocks
     result = blocks_used
     return result

print(solution())