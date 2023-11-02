def solution():
     weekly_allowance = 30
     spent_on_junk_food= weekly_allowance / 3
     spent_on_sweets = 8
     saved = weekly_allowance - spent_on_junk_food - spent_on_sweets
     return saved

print(solution())