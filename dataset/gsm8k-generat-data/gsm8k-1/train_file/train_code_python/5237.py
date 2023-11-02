def solution():
    """For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?"""
    cans = 144
    newspapers = 20
    cans_money = (cans // 12) * 0.5
    newspaper_money = (newspapers // 5) * 1.5
    total_money = cans_money + newspaper_money
    result = total_money
    return result

print(solution())