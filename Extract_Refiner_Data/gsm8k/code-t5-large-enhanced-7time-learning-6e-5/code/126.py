def solution():
    
    # Define the initial number of elves
    initial_elves = 60

    # Calculate the number of elves who quit after children vomit
    children_quit = initial_elves // 3

    # Calculate the number of remaining elves
    remaining_elves = initial_elves - children_quit

    # Calculate the number of elves who quit after kids kick their shins
    kids_quit = remaining_elves // 10

    # Calculate the final number of elves left
    final_elves = remaining_elves - kids_quit

    # Display the final number of elves left
    result = final_elves
    return result

print(solution())