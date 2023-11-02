def solution():
    cost_smartphone = 300
    cost_personal_computer = cost_smartphone + 500
    cost_tablet = cost_smartphone + cost_personal_computer
    result = cost_smartphone + cost_personal_computer + cost_tablet
    return result

print(solution())