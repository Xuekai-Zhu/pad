def solution():
    # Find the number of marbles Archie had initially
    remaining_marbles_after_street = 20 / 0.2  # Since 60% of marbles are lost on the street, he has 40% left
    initial_marbles = remaining_marbles_after_street * 2  # After losing half down a sewer, he has half remaining
    result = initial_marbles
    return result

print(solution())