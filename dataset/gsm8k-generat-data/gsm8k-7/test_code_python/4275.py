def solution():
    ken_funds = 600
    mary_funds = ken_funds * 5
    scott_funds = mary_funds / 3
    total_funds = ken_funds + mary_funds + scott_funds
    goal = 4000
    excess = total_funds - goal
    result = excess
    return result

print(solution())