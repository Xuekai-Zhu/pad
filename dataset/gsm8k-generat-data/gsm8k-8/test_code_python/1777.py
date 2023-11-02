def solution():
    # Calculate the number of basketballs including those with hoops and those on their own
    basketballs_with_hoops = 0.5 * 60
    basketballs_on_their_own = 300 - 60 - 120 - 50 - 40
    total_basketballs = basketballs_with_hoops + basketballs_on_their_own

    result = total_basketballs
    return result

print(solution())