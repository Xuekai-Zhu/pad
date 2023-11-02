def solution():
    """Barry has $10.00 worth of dimes. His little brother, Dan has half that amount but finds 2 more dimes on his way home from school. How many dimes does Dan have?"""
    barry_dime_value = 0.1
    barry_dime_amount = 100 / 10
    barry_total_value = barry_dime_value * barry_dime_amount
    dan_total_value = (barry_total_value / 2) + (2 * barry_dime_value)
    dan_dime_amount = dan_total_value / barry_dime_value
    result = dan_dime_amount
    return result

print(solution())