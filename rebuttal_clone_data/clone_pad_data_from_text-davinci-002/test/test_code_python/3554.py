def solution():
     jars = 16
     clay_pots = jars / 2
     marbles_per_jar = 5
     marbles_per_clay_pot = marbles_per_jar * 3
     total_marbles = jars * marbles_per_jar + clay_pots * marbles_per_clay_pot
     result = total_marbles
     return result

print(solution())