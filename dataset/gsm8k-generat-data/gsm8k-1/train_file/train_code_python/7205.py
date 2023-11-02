def solution():
    """Yvonne brings a box of chocolates to school. Half have nuts and half do not. The students eat 80% of the ones with nuts and eat half of the ones without nuts. If there are 28 chocolates left, how many chocolates were in the box?"""
    chocolates_left = 28
    nuts_chocolates = chocolates_left / 0.2
    non_nuts_chocolates = nuts_chocolates
    total_chocolates = nuts_chocolates + non_nuts_chocolates
    result = total_chocolates
    return result

print(solution())