def solution():
     marbles_initial = 24
     marbles_lost = 4
     marbles_gained = marbles_lost * 2
     marbles_eaten = marbles_lost / 2
     net_marbles = marbles_initial + marbles_gained - marbles_eaten
     result = net_marbles
     return result

print(solution())