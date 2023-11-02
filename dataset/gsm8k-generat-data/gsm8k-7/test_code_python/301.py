def solution():
    total_students = 240

    # Calculate the number of students who read 3 or more novels
    num_three_or_more = total_students * (1 / 6)

    # Calculate the number of students who read 2 novels
    num_two = total_students * 0.35

    # Calculate the number of students who read 1 novel
    num_one = total_students * (5 / 12)

    # Calculate the total number of students who read novels
    total_readers = num_three_or_more + num_two + num_one

    # Calculate the number of students who do not read novels
    num_none = total_students - total_readers
    result = num_none
    return result

print(solution())