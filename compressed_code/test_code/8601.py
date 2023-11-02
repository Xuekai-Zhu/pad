def solution():
    
    total_fights = 190
    knockout_percent = 50
    first_round_percent = 20
    knockouts = total_fights * (knockout_percent / 100)
    first_round_knockouts = knockouts * (first_round_percent / 100)
    result = first_round_knockouts
    return result

print(solution())