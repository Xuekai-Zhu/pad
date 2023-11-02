def solution():
    clear_percent = 40
    black_percent = 20
    other_percent = 100 - clear_percent - black_percent
    num_marbles = 100  # Let's assume Percius has 100 marbles
    num_clear_marbles = (clear_percent / 100) * num_marbles
    num_black_marbles = (black_percent / 100) * num_marbles
    num_other_marbles = num_marbles - num_clear_marbles - num_black_marbles
    num_marbles_taken = 5
    # On average, Percius's friend will get this proportion of other color marbles
    proportion_other_marbles = num_other_marbles / (num_marbles - num_marbles_taken)
    # The friend will end up getting this many other color marbles on average
    num_other_marbles_taken = proportion_other_marbles * (num_marbles_taken)
    result = num_other_marbles_taken
    return result

print(solution())