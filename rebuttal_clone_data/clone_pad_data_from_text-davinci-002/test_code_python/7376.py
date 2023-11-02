def solution():
    days_camping = 5
    pieces_jerky = 40
    pieces_eaten = days_camping * 3
    pieces_left = pieces_jerky - pieces_eaten
    pieces_given = pieces_left / 2
    result = pieces_left - pieces_given
    return result

print(solution())