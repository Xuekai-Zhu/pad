def solution():
    """Bill has 6 times as many nuts as Harry, and Harry has twice as many nuts as Sue. If Sue has 48 nuts, how many do Bill and Harry have combined?"""
    sue_nuts = 48
    harry_nuts = 2 * sue_nuts
    bill_nuts = 6 * harry_nuts
    total_nuts = harry_nuts + bill_nuts
    result = total_nuts
    return result

print(solution())