def solution():
    """Lady Bird uses 1 1/4 cup flour to make 9 biscuits.She’s hosting this month's Junior League club which has 18 members and wants to make sure she allows 2 biscuits per guest. How many cups of flour will Lady Bird need?"""
    flour_per_biscuit = 1.25 / 9
    biscuits_needed = 18 * 2
    flour_needed = flour_per_biscuit * biscuits_needed
    result = flour_needed
    return result

print(solution())