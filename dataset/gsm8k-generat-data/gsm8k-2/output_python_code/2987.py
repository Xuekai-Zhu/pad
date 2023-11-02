def solution():
    """Hadassah took six hours to paint 12 paintings. What would be the total time she's taken to finish all the paintings if she paints 20 more paintings?"""
    paintings_per_hour = 12 / 6
    additional_paintings = 20
    total_paintings = 12 + additional_paintings
    total_time = total_paintings / paintings_per_hour
    result = total_time
    return result

print(solution())