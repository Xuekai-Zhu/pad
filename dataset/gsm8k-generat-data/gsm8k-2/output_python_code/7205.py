def solution():
    """Yvonne brings a box of chocolates to school. Half have nuts and half do not. The students eat 80% of the ones with nuts and eat half of the ones without nuts. If there are 28 chocolates left, how many chocolates were in the box?"""
    nuts_chocolates = total_chocolates = x
    plain_chocolates = total_chocolates = x
    nuts_eaten = 0.8 * nuts_chocolates
    plain_eaten = 0.5 * plain_chocolates
    remaining_chocolates = 28
    remaining_nuts = nuts_chocolates - nuts_eaten
    remaining_plain = plain_chocolates - plain_eaten
    total_nuts = remaining_nuts / 0.2
    total_plain = remaining_plain * 2
    total_chocolates = total_nuts + total_plain
    result = total_chocolates
    return result

print(solution())