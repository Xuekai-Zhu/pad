def solution():
    total_frogs = 5 + 2 + 2 + 18  # Calculate the total number of frogs Francine caught
    mutated_frogs = 5 + 2 + 2  # Calculate the total number of mutated frogs
    mutation_percentage = (mutated_frogs / total_frogs) * 100  # Calculate the percentage of mutated frogs
    rounded_percentage = round(mutation_percentage)  # Round the percentage to the nearest integer
    result = rounded_percentage
    return result

print(solution())