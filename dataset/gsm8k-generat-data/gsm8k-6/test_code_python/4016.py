def solution():
    # Calculate the actual number of animals in the petting zoo
    sheep_count = 7
    pig_count = -3  # Mary forgot to count 3 pigs, so we subtract them
    total_count = 60
    actual_count = total_count - (sheep_count / 2) + pig_count

    result = actual_count
    return result

print(solution())