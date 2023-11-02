def solution():
    current_marbles = 30
    brother_marbles = 60
    sister_marbles = brother_marbles * 2
    friend_marbles = current_marbles * 3

    # Calculate the total number of marbles that Miriam had before giving any away
    total_marbles = current_marbles + brother_marbles + sister_marbles + friend_marbles

    result = total_marbles
    return result

print(solution())