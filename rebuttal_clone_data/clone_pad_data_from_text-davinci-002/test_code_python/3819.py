def solution():
     old_necklaces = 50
     broken_necklaces = 3
     new_necklaces = 5
     necklaces_given_away = 15
     total_necklaces = old_necklaces + new_necklaces - broken_necklaces - necklaces_given_away
     result = total_necklaces
     return result

print(solution())