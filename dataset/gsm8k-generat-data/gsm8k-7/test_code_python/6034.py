def solution():
    # Brendan's catches
    morning_catch = 8
    small_fish = 3
    afternoon_catch = 5
    brendan_total = morning_catch - small_fish + afternoon_catch

    # Brendan's dad's catch
    dad_catch = 13

    # Total catch
    total_catch = brendan_total + dad_catch
    result = total_catch
    return result

print(solution())