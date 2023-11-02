def solution():
    cans_before = 22  # Tim has 22 cans of soda
    cans_after = cans_before - 6  # Jeff takes 6 cans of soda
    cans_bought = (cans_after / 2)  # Tim buys half the amount of soda cans he had left
    total_cans = cans_after + cans_bought  # Total cans of soda Tim has in the end
    result = total_cans
    return result

print(solution())