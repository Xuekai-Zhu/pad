def solution():
     Marco = 24
     Mary = 15
     Mary_after_gift = Marco / 2 + Mary
     Mary_after_spending = Mary_after_gift - 5
     Marco_after_spending = Marco - 5
     final_result = Mary_after_spending - Marco_after_spending
     return final_result

print(solution())