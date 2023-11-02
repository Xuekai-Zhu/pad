def solution():
    """Annie is a mother of 3 children: Mark, Matt, and Mike. She decided to give them some fruits. Mike received 3 oranges. Matt got twice as many apples, and Mark got as many bananas as Mike and Matt received fruits altogether. How many fruits do the three children have in total?"""
    oranges = 3
    apples = 2 * oranges
    total_fruits = oranges + apples + (oranges + apples)
    result = total_fruits
    return result

print(solution())