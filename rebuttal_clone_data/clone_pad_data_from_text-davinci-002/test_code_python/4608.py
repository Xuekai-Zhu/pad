def solution():
    cost_to_enter = 10
    minutes = 2
    drums_hit = 200
    money_made = minutes * (drums_hit - 200) *0.025
    lost = cost_to_enter - money_made
    result = lost / 0.025
    return result

print(solution())