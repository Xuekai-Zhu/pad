def solution():
     initial_marbles = 26
     marbles_found = 6
     marbles_lost = 10
     marbles_gained = marbles_lost * 2
     total_marbles = initial_marbles + marbles_found + marbles_gained
     result = total_marbles
     return result

print(solution())