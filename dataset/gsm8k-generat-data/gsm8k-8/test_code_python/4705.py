def solution():
    # Define the amount of meat Jackson started with
    initial_meat = 20

    # Calculate the amount of meat used for meatballs
    meatballs_meat = initial_meat * (1/4)

    # Calculate the amount of meat left after making meatballs
    remaining_meat = initial_meat - meatballs_meat

    # Subtract the amount of meat used for spring rolls
    final_meat = remaining_meat - 3
    result = final_meat
    return result

print(solution())