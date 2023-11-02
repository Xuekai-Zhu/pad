def solution():
    """At Hank’s cafe, he sells big stack pancakes which have 5 pancakes and short stack pancakes which have 3 pancakes.  If 9 customers order the short stack and 6 customers order the big stack, how many pancakes does Hank need to make?"""
    # Define the number of pancakes in each type of stack
    BIG_STACK_PANCAKES = 5
    SHORT_STACK_PANCAKES = 3

    # Define the number of customers who order each type of stack
    big_stack_customers = 6
    short_stack_customers = 9

    # Calculate the total number of pancakes needed
    total_pancakes = big_stack_customers * BIG_STACK_PANCAKES + short_stack_customers * SHORT_STACK_PANCAKES

    # Display the total number of pancakes needed
    result = total_pancakes
    return result

print(solution())