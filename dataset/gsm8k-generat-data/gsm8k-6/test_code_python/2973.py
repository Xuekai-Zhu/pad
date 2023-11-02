def solution():
    # Calculate the number of stuffies Jean keeps
    keeps = 60 * (1/3)

    # Calculate the number of stuffies Jean gives away
    gives_away = 60 - keeps

    # Calculate the number of stuffies Janet gets
    janet_gets = gives_away * (1/4)
    result = janet_gets
    return result

print(solution())