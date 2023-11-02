def solution():
    bottles_count = 80
    bottles_earnings = bottles_count * 0.10
    total_earnings = 15
    cans_earnings = total_earnings - bottles_earnings
    cans_count = cans_earnings / 0.05
    result = cans_count
    return result

print(solution())