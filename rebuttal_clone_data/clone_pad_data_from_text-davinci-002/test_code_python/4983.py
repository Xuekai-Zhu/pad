def solution(hiker_ml, dog_ml, hiker_liters):
    total_ml = (hiker_ml + dog_ml)
    total_hours = hiker_liters * 1000 / total_ml
    return(total_hours)

print(solution())