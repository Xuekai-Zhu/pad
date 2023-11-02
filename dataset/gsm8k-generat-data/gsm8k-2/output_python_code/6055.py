def solution():
    """Paul, Amoura, and Ingrid were to go to a friend's party planned to start at 8:00 a.m. Paul arrived at 8:25. Amoura arrived 30 minutes later than Paul, and Ingrid was three times later than Amoura. How late, in minutes, was Ingrid to the party?"""
    paul_arrival_time = 8 * 60 + 25
    amoura_arrival_time = paul_arrival_time + 30
    ingrid_arrival_time = amoura_arrival_time + 3 * 30
    party_start_time = 8 * 60
    minutes_late = ingrid_arrival_time - party_start_time
    result = minutes_late
    return result

print(solution())