def solution():
    elephant_exodus = 2880
    hours_elapsed = 11
    elephants_remaining = 28980
    elephant_entrance = (elephants_remaining - (elephant_exodus * hours_elapsed)) / (7)
    result = elephant_entrance
    return result

print(solution())