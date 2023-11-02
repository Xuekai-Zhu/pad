def solution():
     sundaes_on_monday = 40
     m&ms_on_monday = 6
     sundaes_on_tuesday = 20
     m&ms_on_tuesday = 10
     total_m&ms = (sundaes_on_monday * m&ms_on_monday) + (sundaes_on_tuesday * m&ms_on_tuesday)
     total_packs = total_m&ms / 40
     result = total_packs
     return result

print(solution())