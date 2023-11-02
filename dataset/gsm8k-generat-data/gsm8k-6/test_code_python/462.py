def solution():
    # Calculate the total number of skips by Roberto and Valerie in 15 minutes
    skips_Roberto = 4200 * 0.25  # Roberto can skip 4200 times an hour or 70 times in 15 minutes (0.25 hours)
    skips_Valerie = 80 * 15  # Valerie can skip 80 times a minute or 1200 times in 15 minutes
    total_skips = skips_Roberto + skips_Valerie
    result = total_skips
    return result

print(solution())