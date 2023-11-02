def solution():
    Henrys_shells = 11
    Johns_shells = 24
    total_shells = 59
    Leo_collected = total_shells - (Henrys_shells + Johns_shells) 
    Leo_gave_away = Leo_collected / 4
    shells_after_gift = Leo_collected - Leo_gave_away
    total_shells_after_gift = total_shells - Leo_gave_away
    result = total_shells_after_gift
    return result

print(solution())