def solution():
    num_kitchen_bulbs = 35
    broken_kitchen_bulbs = 3/5 * num_kitchen_bulbs
    num_foyer_bulbs = 3 * 10 / (1/3) # find total number of foyer bulbs using the fact that 1/3 are broken
    broken_foyer_bulbs = 10
    # find the number of bulbs that are broken in both foyer and kitchen
    broken_both = broken_kitchen_bulbs * (broken_foyer_bulbs / num_foyer_bulbs)
    # subtract the number of broken bulbs from the total number of bulbs to get the number that are not broken
    not_broken = num_kitchen_bulbs + num_foyer_bulbs - broken_both - broken_kitchen_bulbs - broken_foyer_bulbs
    result = not_broken
    return result

print(solution())