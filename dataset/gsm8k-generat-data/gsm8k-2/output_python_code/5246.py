def solution():
    """Grant spends $200.00 a year to have the newspaper delivered daily to his house. Juanita buys the newspaper daily. Monday through Saturday, she spends $0.50 and on Sunday she spends $2.00. How much more money does Juanita spend buying the newspaper yearly than Grant?"""
    grant_cost = 200
    juanita_cost = ((0.50 * 6) + 2) * 52
    diff = juanita_cost - grant_cost
    result = diff
    return result

print(solution())