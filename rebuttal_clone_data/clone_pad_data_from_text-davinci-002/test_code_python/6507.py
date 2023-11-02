def solution():
     total_sheets = 2450
     binders = 5
     evenly_split_binders = total_sheets / binders
     sheets_used = evenly_split_binders / 2
     result = sheets_used
     return result

print(solution())