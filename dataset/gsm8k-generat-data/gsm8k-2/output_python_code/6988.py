def solution():
    """An artist spends 30 hours every week painting. If it takes her 3 hours to complete a painting, how many paintings can she make in four weeks?"""
    hours_per_week = 30
    hours_per_painting = 3
    paintings_per_week = hours_per_week // hours_per_painting
    total_paintings = paintings_per_week * 4
    result = total_paintings
    return result

print(solution())