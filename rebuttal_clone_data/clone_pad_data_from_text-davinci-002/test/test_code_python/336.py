def solution():
     cans_needed = 100
     cans_collected_by_a = 30
     cans_collected_by_b = 43
     cans_remaining = cans_needed - (cans_collected_by_a + cans_collected_by_b)
     result = cans_remaining
     return result

print(solution())