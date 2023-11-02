def solution():
    # Count the number of papal origins from each country
    spain_origins = 2
    poland_origins = 1
    # Determine if Spain is the least represented country in papal history
    if spain_origins < poland_origins:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())