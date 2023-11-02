def solution():
    ham_per_sandwich = 3  # Anna puts 3 slices of ham in each sandwich
    slices_of_ham = 31  # Anna has 31 slices of ham
    sandwiches_needed = 50  # Anna needs to make 50 ham sandwiches

    # Calculate the total number of slices of ham needed for the sandwiches
    ham_needed = ham_per_sandwich * sandwiches_needed

    # Calculate the difference between the slices of ham Anna has and the slices needed for the sandwiches
    ham_shortage = ham_needed - slices_of_ham
    result = ham_shortage
    return result

print(solution())