def solution():
    """Barry has $10.00 worth of dimes. His little brother, Dan has half that amount but finds 2 more dimes on his way home from school. How many dimes does Dan have?"""
    barry_dollars = 10
    barry_dime_count = barry_dollars / 0.10
    dan_dime_count = (barry_dime_count / 2) + 2
    result = dan_dime_count
    return result

print(solution())