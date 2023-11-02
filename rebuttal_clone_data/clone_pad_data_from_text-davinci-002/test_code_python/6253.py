def solution():
     total_lickers = 4
     licks_by_dan = 58
     licks_by_micheal = 63
     licks_by_sam = 70
     licks_by_david = 70
     licks_by_lance = 39
     total_licks = licks_by_dan + licks_by_micheal + licks_by_sam + licks_by_david + licks_by_lance
     average_licks = total_licks / total_lickers
     result = average_licks
     return result

print(solution())