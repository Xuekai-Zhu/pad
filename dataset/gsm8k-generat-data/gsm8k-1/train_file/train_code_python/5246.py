def solution():
    """
    Grant spends $200.00 a year to have the newspaper delivered daily to his house. 
    Juanita buys the newspaper daily. Monday through Saturday, she spends $0.50 
    and on Sunday she spends $2.00. How much more money does Juanita spend buying the 
    newspaper yearly than Grant?
    """
    grant_cost = 200.00
    juanita_weekday_cost = 0.50 * 6
    juanita_sunday_cost = 2.00
    juanita_total_cost = (juanita_weekday_cost * 365) + (juanita_sunday_cost * 52)
    difference = juanita_total_cost - grant_cost
    result = difference
    return result

print(solution())