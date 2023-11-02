def solution():
    
    ken_funds = 600
    mary_funds = ken_funds * 5
    scott_funds = mary_funds / 3
    total_funds = ken_funds + mary_funds + scott_funds
    excess_funds = total_funds - 4000
    result = excess_funds
    return result

print(solution())