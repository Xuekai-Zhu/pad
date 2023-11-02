def solution():
    cost = 30  # cost of heating pad
    uses_per_week = 3  # number of times John uses it per week
    weeks = 2  # number of weeks John uses it
    total_uses = uses_per_week * weeks  # total number of times John uses it
    cost_per_use = cost / total_uses  # cost per use
    result = cost_per_use
    return result

print(solution())