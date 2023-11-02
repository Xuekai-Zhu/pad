def solution():
    apples_picked = 34
    apples_needed_per_pie = 4
    unripe_apples = 6
    ripe_apples = apples_picked - unripe_apples
    pies_that_can_be_made = ripe_apples / apples_needed_per_pie
    result = pies_that_can_be_made
    return result

print(solution())