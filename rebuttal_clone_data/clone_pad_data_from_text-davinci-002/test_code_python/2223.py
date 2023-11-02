def solution():
     gum_pieces = 100
     gum_given_away = gum_pieces / 2
     gum_pieces_left = gum_given_away / 2
     gum_chewed = 11
     gum_left = gum_pieces_left - gum_chewed
     result = gum_left
     return result

print(solution())