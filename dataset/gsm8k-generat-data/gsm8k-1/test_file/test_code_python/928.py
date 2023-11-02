def solution():
    """Maria invited 4 of her friends over for a water balloon fight in the backyard. At the start of the game, Maria gave each of her friends 2 water balloons. She had one water balloon for herself. Then her mom came out and gave each person 3 more balloons. How many total balloons did the girls have?"""
    num_friends = 4
    balloons_per_person_initial = 2
    balloons_for_maria_initial = 1
    balloons_per_person_added = 3
    total_balloons = (num_friends * balloons_per_person_initial) + balloons_for_maria_initial + (num_friends + 1) * balloons_per_person_added
    result = total_balloons
    return result

print(solution())