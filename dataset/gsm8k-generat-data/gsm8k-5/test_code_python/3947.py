def solution():
    sue_nuts = 48  # Sue has 48 nuts
    harry_nuts = 2 * sue_nuts  # Harry has twice as many nuts as Sue
    bill_nuts = 6 * harry_nuts  # Bill has 6 times as many nuts as Harry

    # Calculate the total number of nuts Bill and Harry have combined
    total_nuts = harry_nuts + bill_nuts
    result = total_nuts
    return result

print(solution())