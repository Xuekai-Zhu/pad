def solution():
    
    total_popsicles = 165
    betty_popsicles = total_popsicles / (5 + 6)
    sam_popsicles = total_popsicles / (6 + 6)
    difference = sam_popsicles - betty_popsicles
    result = difference
    return result

print(solution())