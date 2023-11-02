def solution():
    # Calculate the total number of magazines Alexandra bought initially
    initial_magazines = 8 + 12

    # Calculate the number of magazines Alexandra bought on Sunday
    sunday_magazines = 4 * 8

    # Calculate the total number of magazines Alexandra had before her dog chewed them up
    total_magazines_before_chewing = initial_magazines + sunday_magazines

    # Calculate the final number of magazines Alexandra has after her dog chewed up 4
    final_magazines = total_magazines_before_chewing - 4

    result = final_magazines
    return result

print(solution())