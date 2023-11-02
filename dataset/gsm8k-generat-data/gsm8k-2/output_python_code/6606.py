def solution():
    """Carly is a pet groomer. Today, her task was trimming the four nails on dogs’ paws. She trimmed 164 nails, but three of the dogs had only three legs. How many dogs did Carly work on?"""
    total_nails = 164
    nails_per_dog = 4
    missing_legs = 3
    nails_on_three_legged_dogs = missing_legs * nails_per_dog
    nails_on_four_legged_dogs = total_nails - nails_on_three_legged_dogs
    dogs_with_four_legs = nails_on_four_legged_dogs // nails_per_dog
    total_dogs = dogs_with_four_legs + missing_legs
    result = total_dogs
    return result

print(solution())