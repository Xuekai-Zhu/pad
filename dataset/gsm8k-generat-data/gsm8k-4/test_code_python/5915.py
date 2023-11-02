def solution():
    """Michael bought 6 crates of egg on Tuesday. He gave out 2 crates to Susan, who he admires and bought another 5 crates on Thursday. If one crate holds 30 eggs, how many eggs does he have now?"""
    # Define the number of crates of eggs
    crates_of_eggs = 6

    # Calculate the total number of eggs in the crates
    total_eggs = crates_of_eggs * 30

    # Subtract the 2 crates given to Susan from the total number of eggs
    total_eggs -= 2 * 30

    # Add the 5 crates bought on Thursday to the total number of eggs
    total_eggs += 5 * 30

    # Return the total number of eggs
    result = total_eggs
    return result

print(solution())