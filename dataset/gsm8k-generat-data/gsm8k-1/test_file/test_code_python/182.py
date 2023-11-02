def solution():
    """Russell works at a pet store and is distributing straw among the rodents. The rats are kept in 3 cages in equal groups and each rat is given 6 pieces of straw. There are 10 cages of hamsters that are kept alone and each hamster is given 5 pieces of straw. There is also a pen of rabbits where 20 pieces of straw are distributed among the rabbits. No straw is used anywhere else in the store. If 160 pieces of straw have been distributed among the small rodents, how many rats are in each cage?"""
    rats_per_cage = unknown 
    hamsters_per_cage = 1
    pieces_of_straw_per_rat = 6
    pieces_of_straw_per_hamster = 5
    total_pieces_of_straw = 160
    total_rats = rats_per_cage * 3
    total_hamsters = hamsters_per_cage * 10
    total_rabbits = 20
    total_small_rodents = total_rats + total_hamsters
    total_pieces_of_straw_used = total_rats * pieces_of_straw_per_rat + total_hamsters * pieces_of_straw_per_hamster + total_rabbits
    if total_pieces_of_straw_used == total_pieces_of_straw:
        result = rats_per_cage 
    return result

print(solution())