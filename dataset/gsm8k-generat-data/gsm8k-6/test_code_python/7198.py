def solution():
    # Find the number of marbles that Betty gave to Stuart
    marbles_given = 0.4 * 60

    # Find the number of marbles Stuart had after Betty gave him some
    marbles_stuart = marbles_given + 80

    # Find the number of marbles Stuart had initially
    marbles_initially = marbles_stuart / 0.6

    result = marbles_initially
    return result

print(solution())