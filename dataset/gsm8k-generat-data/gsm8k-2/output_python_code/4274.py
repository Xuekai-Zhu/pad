def solution():
    """Scott, Mary, and Ken committed to raising $4,000 for their local children’s cancer hospital. Right now, Mary’s collection is five times what Ken has, but three times Scott’s funds. If Ken has $600, by how much have the three exceeded their goal?"""
    ken_funds = 600
    mary_funds = 5 * ken_funds
    scott_funds = mary_funds / 3
    total_funds = ken_funds + mary_funds + scott_funds
    excess_funds = total_funds - 4000
    result = excess_funds
    return result

print(solution())