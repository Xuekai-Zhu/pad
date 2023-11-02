def solution():
    norris_savings = [29, 25, 31]
    hugo_spending = 75
    norris_total = sum(norris_savings)
    norris_leftover = norris_total - hugo_spending
    result = norris_leftover
    return result

print(solution())