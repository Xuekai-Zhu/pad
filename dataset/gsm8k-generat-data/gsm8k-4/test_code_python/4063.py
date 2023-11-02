def solution():
    """At Hank’s cafe, he sells big stack pancakes which have 5 pancakes and short stack pancakes which have 3 pancakes. If 9 customers order the short stack and 6 customers order the big stack, how many pancakes does Hank need to make?"""
    # Define the number of pancakes in a big stack and a short stack
    big_stack = 5
    short_stack = 3

    # Calculate the total number of pancakes ordered
    total_pancakes = (6 * big_stack) + (9 * short_stack)

    # return the result
    result = total_pancakes
    return result

print(solution())