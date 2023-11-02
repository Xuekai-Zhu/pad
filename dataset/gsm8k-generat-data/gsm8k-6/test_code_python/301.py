def solution():
    # Calculate the number of students who read three or more novels
    read_three_or_more = (1/6) * 240

    # Calculate the number of students who read two novels
    read_two = 0.35 * 240

    # Calculate the number of students who read one novel
    read_one = (5/12) * 240

    # Calculate the total number of students who read novels
    read_novels = read_three_or_more + read_two + read_one

    # Calculate the number of students who do not read novels
    no_novels = 240 - read_novels
    result = no_novels
    return result

print(solution())