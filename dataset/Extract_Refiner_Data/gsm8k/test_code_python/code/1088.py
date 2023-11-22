def solution():
    
    # Define the amount of meat eaten by the Tyrannosaurus rex
    rex_meat = 270 / 2

    # Calculate the amount of meat left after the Tyrannosaurus rex
    remaining_meat = rex_meat * 2

    # Calculate the amount of meat scavenged by the pack of velociraptors
    velociraptors_meat = remaining_meat / 2

    # Calculate the total amount of meat before the T-Rex ate
    total_meat_before_express = remaining_meat + velociraptors_meat

    # Display the total amount of meat before the T-Rex ate
    result = total_meat_before_express
    return result

print(solution())