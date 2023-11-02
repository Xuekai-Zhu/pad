def solution():
    """Carly is a pet groomer. Today, her task was trimming the four nails on dogs’ paws. She trimmed 164 nails, but three of the dogs had only three legs. How many dogs did Carly work on?"""
    # Define the number of nails on each dog's paw
    nails_per_paw = 4

    # Calculate the total number of nails that would have been trimmed if all dogs had four legs
    total_nails = nails_per_paw * (164/4)

    # Calculate the number of dogs with three legs
    three_legged_dogs = 3

    # Calculate the number of dogs with four legs
    four_legged_dogs = total_nails // nails_per_paw - three_legged_dogs

    # Calculate the total number of dogs
    total_dogs = three_legged_dogs + four_legged_dogs

    # return the result
    result = total_dogs
    return result

print(solution())