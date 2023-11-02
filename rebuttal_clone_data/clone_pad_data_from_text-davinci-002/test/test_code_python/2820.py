def solution():
     bowl_1_capacity = 3/4
     bowl_2_capacity = 1
     bowl_2_marbles = 600
     bowl_1_marbles = bowl_2_marbles * bowl_1_capacity
     total_marbles = bowl_1_marbles + bowl_2_marbles
     
     return total_marbles

print(solution())