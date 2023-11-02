def solution():
    
    hours_per_12_paintings = 6
    paintings_to_paint = 32
    hours_per_painting = hours_per_12_paintings / 12
    total_hours = hours_per_painting * paintings_to_paint
    result = total_hours
    return result

print(solution())