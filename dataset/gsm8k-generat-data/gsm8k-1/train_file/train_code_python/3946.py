def solution():
    """Bill has 6 times as many nuts as Harry, and Harry has twice as many nuts as Sue. If Sue has 48 nuts, how many do Bill and Harry have combined?"""
    sue_nuts = 48
    harry_nuts = sue_nuts * 2
    bill_nuts = harry_nuts * 6
    combined_nuts = harry_nuts + bill_nuts
    result = combined_nuts
    return result

print(solution())