def solution():
    # Zack's marbles can be divided equally among 3 people, leaving him with 5 marbles
    # This means that the total number of marbles must be 3x + 5, where x is a whole number
    # After giving his friends 20 marbles each and keeping 5, Zack is left with 3x - 55 marbles
    # This must be equal to the original number of marbles (3x + 5)
    # So we can solve for x: 3x - 55 = 3x + 5 => x = 30

    # Therefore, the initial number of marbles Zack had was: 3x + 5 = 3(30) + 5 = 95
    initial_marbles = 95
    result = initial_marbles
    return result

print(solution())