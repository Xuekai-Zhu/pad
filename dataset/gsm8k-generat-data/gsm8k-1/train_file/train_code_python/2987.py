def solution():
    """Hadassah took six hours to paint 12 paintings. What would be the total time she's taken to finish all the paintings if she paints 20 more paintings?"""
    hours_per_12_paintings = 6
    paintings_to_paint = 32
    hours_per_painting = hours_per_12_paintings / 12
    total_hours = hours_per_painting * paintings_to_paint
    result = total_hours
    return result

print(solution())