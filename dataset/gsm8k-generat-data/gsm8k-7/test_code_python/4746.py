def solution():
    set1_size = 50
    set1_broken_perc = 0.1

    set2_size = 60
    set2_broken_perc = 0.2

    # Calculate the number of broken marbles in each set
    set1_broken = set1_size * set1_broken_perc
    set2_broken = set2_size * set2_broken_perc

    # Calculate the total number of broken marbles
    total_broken = set1_broken + set2_broken

    result = total_broken
    return result

print(solution())