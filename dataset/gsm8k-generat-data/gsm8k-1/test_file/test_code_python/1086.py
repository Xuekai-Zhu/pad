def solution():
    """Caroline has 4 children. The first child is 6 feet tall. The second child is two inches taller than the first child. The third child is 5 inches shorter than the second child. And the fourth child is three inches taller than the third child. How tall is the fourth child, in inches?"""
    first_child = 6 * 12  # convert feet to inches
    second_child = first_child + 2
    third_child = second_child - 5
    fourth_child = third_child + 3
    result = fourth_child
    return result

print(solution())