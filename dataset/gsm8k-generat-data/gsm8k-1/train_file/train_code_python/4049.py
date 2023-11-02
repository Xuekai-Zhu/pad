def solution():
    """Angus, Patrick, and Ollie went fishing for trout on Rainbow Lake. Angus caught 4 more fish than Patrick did, but Ollie caught 7 fewer fish than Angus. If Ollie caught 5 fish, how many fish did Patrick catch?"""
    ollie_catch = 5
    angus_catch = ollie_catch + 7
    patrick_catch = angus_catch - 4
    result = patrick_catch
    return result

print(solution())