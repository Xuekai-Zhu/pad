def solution():
    
    total_posters = 50
    small_posters = (2/5)*total_posters
    medium_posters = (1/2)*total_posters
    large_posters = total_posters - small_posters - medium_posters
    result = large_posters
    return result

print(solution())