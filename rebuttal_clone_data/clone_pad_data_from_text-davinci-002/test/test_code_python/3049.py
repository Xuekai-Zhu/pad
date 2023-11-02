def solution():
     total_posters = 50
     small_posters = total_posters * 2/5
     medium_posters = total_posters * 1/2
     large_posters = total_posters - small_posters - medium_posters
     result = large_posters
     return result

print(solution())