def solution():
    # Define the ratios of fish caught by each person
    ryan_to_jason_ratio = 3
    jeffery_to_ryan_ratio = 2

    # Calculate the number of fish caught by Ryan and Jason
    ryan_catch = 60 / jeffery_to_ryan_ratio
    jason_catch = ryan_catch / ryan_to_jason_ratio

    # Calculate the total number of fish caught
    total_catch = ryan_catch + jason_catch + 60

    result = total_catch
    return result

print(solution())