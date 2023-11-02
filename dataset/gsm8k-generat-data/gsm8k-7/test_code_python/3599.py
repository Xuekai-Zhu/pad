def solution():
    victor_shrimp = 26
    austin_shrimp = victor_shrimp - 8
    total_shrimp = (victor_shrimp + austin_shrimp) / 2
    earnings_per_tail = 7.0 / 11
    total_earnings = total_shrimp * earnings_per_tail
    earnings_per_person = total_earnings / 3
    result = earnings_per_person
    return result

print(solution())