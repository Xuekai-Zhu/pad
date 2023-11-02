def solution():
    vaccine_percent = 33.33  # 1/3 of the town is fully vaccinated
    recovery_percent = 33.33  # 1/3 of the town is immune due to recovery from COVID
    overlap_percent = 16.67  # 1/6 of the town is both vaccinated and already had COVID
    immune_percent = vaccine_percent + recovery_percent - overlap_percent  # Calculate the total percentage of people who are immune
    result = immune_percent
    return result

print(solution())