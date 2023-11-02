def solution():
     total_cats = 16
     white_cats = 2
     black_cats = total_cats * 0.25
     grey_cats = total_cats - white_cats - black_cats
     result = grey_cats
     return result

print(solution())