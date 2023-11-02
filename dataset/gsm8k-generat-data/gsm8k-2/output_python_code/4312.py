def solution():
    """Bob enters cycling competitions every single week and hopes to win the 100 dollar grand prize each time. For the first 2 weeks, he managed first place and got 100 dollars each week. He is saving up for a puppy that costs 1000 dollars. What is the minimum number of additional weeks Bob must win first place?"""
    total_prize_money = 200  # Bob has already won $200
    puppy_cost = 1000
    additional_weeks = (puppy_cost - total_prize_money) // 100 + 1  # Bob needs to win $800 more, so he needs to win at least 8 more competitions
    result = additional_weeks
    return result

print(solution())