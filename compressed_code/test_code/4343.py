def solution():
    
    vaccine_percent = 1/3
    recovery_percent = 1/3
    vaccinated_and_recovered_percent = 1/6
    immune_percent = vaccine_percent + recovery_percent - vaccinated_and_recovered_percent
    result = immune_percent * 100
    return result

print(solution())