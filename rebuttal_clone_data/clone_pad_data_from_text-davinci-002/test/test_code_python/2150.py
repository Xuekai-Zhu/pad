def solution():
    flutes = 20
    clarinets = 30
    trumpets = 60
    pianists = 20
    percent_flutes = 80
    percent_clarinets = 50
    percent_trumpets = 33.3
    percent_pianists = 10
    total_flutes = flutes * (percent_flutes / 100)
    total_clarinets = clarinets * (percent_clarinets / 100)
    total_trumpets = trumpets * (percent_trumpets / 100)
    total_pianists = pianists * (percent_pianists / 100)
    people_in_band = total_flutes + total_clarinets + total_trumpets + total_pianists
    result = people_in_band
    
    return result

print(solution())