def solution():
    total_flavors = 100  # The ice cream shop offers 100 different flavors
    tried_flavors = 1/4 * total_flavors + 2*(1/4 * total_flavors) # Gretchen tried 1/4 of the flavors 2 years ago and double that amount last year
    remaining_flavors = total_flavors - tried_flavors # Gretchen needs to try the remaining flavors

    # Calculate how many more flavors Gretchen will need to try this year to have tried all 100 flavors
    more_flavors = remaining_flavors
    result = more_flavors
    return result

print(solution())