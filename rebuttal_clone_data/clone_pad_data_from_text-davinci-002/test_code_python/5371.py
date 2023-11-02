def solution():
     apples = 20
     apples_to_jane = 5
     apples_to_james = 7
     apples_left = 4
     apples_given_away = apples_to_jane + apples_to_james
     apples_needed = apples_given_away - apples_left
     result = apples_needed
     
     return result

print(solution())