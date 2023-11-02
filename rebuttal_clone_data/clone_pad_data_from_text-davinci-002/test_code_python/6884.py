def solution():
     total_dresses = 24
     dresses_with_pockets = total_dresses / 2
     dresses_with_two_pockets = dresses_with_pockets / 3
     dresses_with_three_pockets = dresses_with_pockets - dresses_with_two_pockets
     total_pockets = (dresses_with_two_pockets * 2) + (dresses_with_three_pockets * 3)
     result = total_pockets
     return result

print(solution())