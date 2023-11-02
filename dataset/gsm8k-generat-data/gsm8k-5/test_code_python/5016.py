def solution():
    total_marbles = 100  # Assume Percius has 100 marbles
    clear_marbles = 0.4 * total_marbles  # 40% of the marbles are clear
    black_marbles = 0.2 * total_marbles  # 20% of the marbles are black
    other_marbles = total_marbles - clear_marbles - black_marbles  # Calculate the number of marbles that are not clear or black
    friend_takes = 5  # Percius's friend takes 5 marbles

    # Calculate the average number of marbles of other colors that Percius's friend will get
    avg_other_marbles = other_marbles * (friend_takes / (total_marbles - friend_takes))
    result = avg_other_marbles
    return result

print(solution())