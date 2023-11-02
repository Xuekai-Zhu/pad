def solution():
    # Calculate the total number of marbles before they take any away
    total_marbles = 12 + 28

    # Calculate how many marbles they each take away
    chris_taken = 1/4 * 12
    ryan_taken = 1/4 * 28

    # Calculate the total number of marbles taken away
    total_taken = chris_taken + ryan_taken

    # Calculate the number of marbles remaining in the pile
    remaining_marbles = total_marbles - total_taken
    result = remaining_marbles
    return result

print(solution())