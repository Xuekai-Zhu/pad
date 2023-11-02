def solution():
    num_posters = 50
    small_posters = (2/5) * num_posters
    medium_posters = (1/2) * num_posters
    large_posters = num_posters - small_posters - medium_posters
    result = large_posters
    return result

print(solution())