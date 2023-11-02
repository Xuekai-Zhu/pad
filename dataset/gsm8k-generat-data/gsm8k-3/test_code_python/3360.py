def solution():
    """At the zoo, there are 5 different types of animals. Seeing each animal type takes around 6 minutes. How much time would it take to see each animal type if the zoo decided to import 4 new species?"""
    # Define the number of animal types and the time to see each type
    num_animals = 5
    time_per_animal = 6

    # Calculate the total time to see the original animal types
    total_time = num_animals * time_per_animal

    # Calculate the total time to see all animal types, including the new ones
    total_animals = num_animals + 4
    total_time_new_animals = total_animals * time_per_animal

    # Calculate the time to see only the new animal types
    time_new_animals = (total_animals - num_animals) * time_per_animal

    # Display the time to see all animal types and the time to see only the new animal types
    result = total_time_new_animals - total_time
    return result

print(solution())