def solution():
    
    # Define the initial amount of meat on the triceratops
    initial_meat = 270

    # Calculate the amount of meat the triceratops had hunted before the T-Rex ate
    rex_ate = initial_meat / 2

    # Calculate the amount of meat the pack of velociraptors had left after the T-Rex ate
    remaining_meat = initial_meat - rex_ate

    # Calculate the amount of meat the pack of velociraptors had scavenged
    scavened_meat = remaining_meat / 2

    # Calculate the final amount of meat on the triceratops
    final_meat = remaining_meat - scavened_meat

    # Display the final amount of meat
    result = final_meat
    return result

print(solution())