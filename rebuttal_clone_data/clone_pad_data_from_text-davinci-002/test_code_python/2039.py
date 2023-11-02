def solution():
     total_marbles = 400
     marbles_per_pack = 10
     packs_of_marbles = total_marbles / marbles_per_pack
     packs_given_to_Manny = packs_of_marbles / 4
     packs_given_to_Neil = packs_of_marbles / 8
     packs_kept = packs_of_marbles - packs_given_to_Manny - packs_given_to_Neil
     result = packs_kept
     return result

print(solution())