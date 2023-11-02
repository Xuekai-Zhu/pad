def solution():
    """Jamaar loves fresh fruit and is headed to the store with $10 he earned mowing lawns. Including tax, peaches and pears are $.5 each, apples are $.75 each, kiwis are $1, and plums cost $.25 each. If he has already purchased 3 peaches, 4 pears, 2 kiwis, and 5 apples, how many plums can he buy?"""
    budget = 10
    peach_price = 0.5
    pear_price = 0.5
    apple_price = 0.75
    kiwi_price = 1
    plum_price = 0.25
    peach_qty = 3
    pear_qty = 4
    apple_qty = 5
    kiwi_qty = 2
    spent_so_far = (peach_qty * peach_price) + (pear_qty * pear_price) + (apple_qty * apple_price) + (kiwi_qty * kiwi_price)
    remaining_budget = budget - spent_so_far
    plum_qty = int(remaining_budget / plum_price)
    result = plum_qty
    return result

print(solution())