def solution():
    # Calculate the total number of eggs Michael has now
    initial_eggs = 6 * 30  # Michael bought 6 crates of eggs, each crate has 30 eggs
    eggs_given_out = 2 * 30  # Michael gave out 2 crates of eggs, each crate has 30 eggs
    eggs_bought = 5 * 30  # Michael bought 5 more crates of eggs, each crate has 30 eggs
    total_eggs = initial_eggs - eggs_given_out + eggs_bought  # calculate the total number of eggs
    result = total_eggs
    return result

print(solution())