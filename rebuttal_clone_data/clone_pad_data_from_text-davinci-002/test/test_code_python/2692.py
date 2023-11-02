def solution():
     set_one_marbles = 50
     set_two_marbles = 60
     set_one_broken_percent = 10
     set_two_broken_percent = 20
     set_one_broken = set_one_marbles * (set_one_broken_percent / 100)
     set_two_broken = set_two_marbles * (set_two_broken_percent / 100)
     total_broken = set_one_broken + set_two_broken
     result = total_broken
     return result

print(solution())