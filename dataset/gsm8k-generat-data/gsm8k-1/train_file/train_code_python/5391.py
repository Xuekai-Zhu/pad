def solution():
    """Marcy can make 3 spears out of a sapling and 9 spears out of a log. How many spears can she make out of 6 saplings and a log?"""
    saplings_per_spear = 3
    logs_per_spear = 9
    
    saplings = 6
    logs = 1
    
    saplings_spears = saplings * saplings_per_spear
    log_spears = logs * logs_per_spear
    
    total_spears = saplings_spears + log_spears
    result = total_spears
    
    return result

print(solution())