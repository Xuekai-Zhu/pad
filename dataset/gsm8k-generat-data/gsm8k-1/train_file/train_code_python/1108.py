def solution():
    """Annie is a mother of 3 children: Mark, Matt, and Mike. She decided to give them some fruits. Mike received 3 oranges. Matt got twice as many apples, and Mark got as many bananas as Mike and Matt received fruits altogether. How many fruits do the three children have in total?"""
    mike_fruits = 3
    matt_fruits = 2 * mike_fruits
    total_fruits = mike_fruits + matt_fruits
    mark_fruits = total_fruits
    all_fruits = mike_fruits + matt_fruits + mark_fruits
    result = all_fruits
    return result

print(solution())