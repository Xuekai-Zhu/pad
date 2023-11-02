def solution():
    """One meatball sub sandwich contains 4 meatballs. Sidney ordered 3 less than ten meatball sub sandwiches. Then
    Mark ate 4 of Sidney’s meatball sub sandwiches. So Sidney ordered another three sub sandwiches. How many meatballs
    were in the sub sandwiches that remained?"""

    meatballs_per_sandwich = 4
    initial_order = 10 - 3
    mark_ate = 4
    sidney_ordered_more = 3
    remaining_sandwiches = initial_order - mark_ate + sidney_ordered_more
    remaining_meatballs = remaining_sandwiches * meatballs_per_sandwich
    result = remaining_meatballs
    return result

print(solution())