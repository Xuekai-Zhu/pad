def solution():
     hats = 4
     cloaks = 3
     needed_for_hats = hats / 1
     needed_for_cloaks = cloaks / 3
     total_needed = needed_for_hats + (needed_for_cloaks * 6)
     result = total_needed
     return result

print(solution())