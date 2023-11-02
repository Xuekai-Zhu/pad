def solution():
    """Bob enters cycling competitions every single week and hopes to win the 100 dollar grand prize each time. For the first 2 weeks, he managed first place and got 100 dollars each week. He is saving up for a puppy that costs 1000 dollars. What is the minimum number of additional weeks Bob must win first place?"""
    initial_money = 200
    goal = 1000
    each_win = 100
    remaining_goal = goal - initial_money
    additional_wins = remaining_goal / each_win
    result = int(additional_wins) + 2
    return result

print(solution())