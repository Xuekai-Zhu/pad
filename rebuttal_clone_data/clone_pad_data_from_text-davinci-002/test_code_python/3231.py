def solution():
     pieces_of_bread = 200
     pieces_eaten_1 = pieces_of_bread * (1/4)
     pieces_left_1 = pieces_of_bread - pieces_eaten_1
     pieces_eaten_2 = pieces_left_1 * (2/5)
     pieces_left_2 = pieces_left_1 - pieces_eaten_2
     pieces_eaten_3 = pieces_left_2 * (1/2)
     pieces_left_3 = pieces_left_2 - pieces_eaten_3
     result = pieces_left_3
     return result

print(solution())