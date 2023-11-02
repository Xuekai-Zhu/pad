def solution():
    """Janet has 24 dresses. Half of them have pockets. Of those, a third have 2 pockets and the rest have 3 pockets. How many total pockets do her dresses have?"""
    total_dresses = 24
    dresses_with_pockets = total_dresses / 2
    dresses_with_2pockets = dresses_with_pockets / 3
    dresses_with_3pockets = dresses_with_pockets - dresses_with_2pockets
    total_pockets = (dresses_with_2pockets * 2) + (dresses_with_3pockets * 3)
    result = total_pockets
    return result

print(solution())