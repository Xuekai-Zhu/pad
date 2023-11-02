def solution():
     selfies_last_year = 10
     selfies_this_year = 17
     total_photos = 2430
     selfies_total = selfies_last_year + selfies_this_year
     selfies_this_year = (selfies_this_year / selfies_total) * total_photos
     selfies_last_year = (selfies_last_year / selfies_total) * total_photos
     result = selfies_this_year - selfies_last_year
     return result

print(solution())