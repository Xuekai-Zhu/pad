def solution():
     shirts_sewn_on_monday = 4
     shirts_sewn_on_tuesday = 3
     shirts_sewn_on_wednesday = 2
     buttons_per_shirt = 5
     total_buttons = (shirts_sewn_on_monday * buttons_per_shirt) + (shirts_sewn_on_tuesday * buttons_per_shirt) + (shirts_sewn_on_wednesday * buttons_per_shirt)
     result = total_buttons
     return result

print(solution())