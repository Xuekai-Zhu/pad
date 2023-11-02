def solution():
    ham_per_sandwich = 3
    current_ham_slices = 31
    sandwiches_needed = 50

    ham_needed = sandwiches_needed * ham_per_sandwich
    more_ham_needed = ham_needed - current_ham_slices
    result = more_ham_needed
    return result

print(solution())