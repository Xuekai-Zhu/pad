def solution():
    """Angus, Patrick, and Ollie went fishing for trout on Rainbow Lake. Angus caught 4 more fish than Patrick did, but Ollie caught 7 fewer fish than Angus. If Ollie caught 5 fish, how many fish did Patrick catch?"""
    ollie_fish = 5
    angus_fish = ollie_fish + 7
    patrick_fish = angus_fish - 4
    result = patrick_fish
    return result

print(solution())