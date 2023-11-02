def solution():
    """Nick had twice as many candies as George. Then George ate 5 candies. Now George has 3 candies left. How many candies does Nick have?"""
    george_candies = 3
    george_initial = george_candies + 5
    nick_candies = george_initial * 2
    result = nick_candies
    return result

print(solution())