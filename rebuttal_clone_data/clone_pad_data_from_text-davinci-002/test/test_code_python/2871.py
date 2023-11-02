def solution():
    notes_per_day = 2
    days_per_week = 5
    classes = 5
    weeks = 6
    sheets_per_pack = 100
    total_notes = notes_per_day * days_per_week * classes * weeks
    total_packs = total_notes / sheets_per_pack
    result = total_packs
    return result

print(solution())