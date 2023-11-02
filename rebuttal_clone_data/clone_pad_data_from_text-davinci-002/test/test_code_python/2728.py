def solution():
     total_people = 100
     blue_eyed = 19
     brown_eyed = total_people / 2
     black_eyed = total_people / 4
     green_eyed = total_people - (blue_eyed + brown_eyed + black_eyed)
     result = green_eyed
     return result

print(solution())