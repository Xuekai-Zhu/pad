def solution():
     state_quarters = 50
     quarters_doubled = state_quarters * 2
     quarters_collected_1 = quarters_doubled + (3 * 12)
     quarters_collected_2 = quarters_collected_1 + (1 * 4)
     quarters_lost = quarters_collected_2 / 4
     quarters_remaining = quarters_collected_2 - quarters_lost
     result = quarters_remaining
     return result

print(solution())