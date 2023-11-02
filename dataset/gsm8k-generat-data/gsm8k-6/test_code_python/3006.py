def solution():
    # Calculate the number of flavors Gretchen has tried so far
    tried_flavors = 100 * (1/4) * 2 + 100 * (1/2) # Gretchen tried 1/4 of the flavors 2 years ago and double that amount last year

    # Calculate the number of flavors Gretchen still needs to try
    remaining_flavors = 100 - tried_flavors
    result = remaining_flavors
    return result

print(solution())