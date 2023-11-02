def solution():
     blocks_per_minute = 2
     minutes_per_block = 1.5
     blocks_to_home = 8
     minutes_to_home = blocks_to_home / blocks_per_minute * minutes_per_block
     result = minutes_to_home
     return result

print(solution())