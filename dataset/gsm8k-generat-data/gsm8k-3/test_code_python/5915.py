def solution():
    """Michael bought 6 crates of egg on Tuesday. He gave out 2 crates to Susan, who he admires and bought another 5 crates on Thursday. If one crate holds 30 eggs, how many eggs does he have now?"""
    # Calculate the number of eggs Michael had initially
    initial_eggs = 6 * 30

    # Calculate the number of eggs he gave to Susan
    given_eggs = 2 * 30

    # Calculate the number of eggs he bought on Thursday
    bought_eggs = 5 * 30

    # Calculate the total number of eggs he has now
    total_eggs = initial_eggs - given_eggs + bought_eggs

    # Display the total number of eggs
    result = total_eggs
    return result

print(solution())