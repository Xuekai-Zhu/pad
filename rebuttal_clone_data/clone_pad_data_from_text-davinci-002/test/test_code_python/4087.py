def solution():
     total_pieces = 60
     pieces_taken_by_michael = total_pieces / 2
     pieces_left = total_pieces - pieces_taken_by_michael
     pieces_taken_by_paige = pieces_left / 2
     pieces_taken_by_mandy = pieces_left - pieces_taken_by_paige
     result = pieces_taken_by_mandy
     return result

print(solution())