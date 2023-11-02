def solution():
    # Find the number of stuffies Jean keeps for herself
    jean_keeps = 60 * (1/3)

    # Calculate how many stuffies Jean gives away
    jean_gives_away = 60 - jean_keeps

    # Calculate how many stuffies Janet gets
    janet_gets = jean_gives_away * (1/4)
    result = janet_gets
    return result

print(solution())