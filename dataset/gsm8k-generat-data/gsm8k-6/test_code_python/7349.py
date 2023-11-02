def solution():
    # Calculate the total number of cups of sugar used
    sugar_ratio = 1/(1+2)  # ratio of sugar in the mixture
    total_cups = 84  # total cups of the mixture used
    cups_of_sugar = sugar_ratio * total_cups  # cups of sugar used
    result = cups_of_sugar
    return result

print(solution())