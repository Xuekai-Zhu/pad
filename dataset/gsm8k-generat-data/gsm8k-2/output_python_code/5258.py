def solution():
    """I caught 4 fewer fish than the number in my tank and added them to my fish tank. If the tank has 20 fish right now, how many did I add?"""
    current_fish = 20
    caught_fish = current_fish - 4
    added_fish = current_fish - caught_fish
    result = added_fish
    return result

print(solution())