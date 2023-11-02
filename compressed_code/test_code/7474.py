def solution():
    
    martha_cans = 90
    diego_cans = (martha_cans / 2) + 10
    total_cans = 150
    cans_needed = total_cans - (martha_cans + diego_cans)
    result = cans_needed
    return result

print(solution())