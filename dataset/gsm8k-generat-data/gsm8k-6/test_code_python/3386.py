def solution():
    # Calculate the total number of times the terrier barked
    terrier_barks = 6 * 2 + 6  # the terrier barked every second time and was hushed six times before the dogs stopped

    # Calculate the total number of times the poodle barked
    poodle_barks = 2 * terrier_barks

    result = poodle_barks
    return result

print(solution())