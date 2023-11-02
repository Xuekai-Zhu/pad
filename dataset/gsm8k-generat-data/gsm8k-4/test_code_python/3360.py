def solution():
    """At the zoo, there are 5 different types of animals. Seeing each animal type takes around 6 minutes. How much time would it take to see each animal type if the zoo decided to import 4 new species?"""
    # Define the number of animal types and the time to see each type
    num_animal_types = 5
    time_per_type = 6

    # Add the time to see the new animal types
    total_time = (num_animal_types + 4) * time_per_type

    # Return the result
    result = total_time
    return result

print(solution())