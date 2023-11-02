def solution():
    """Carly is a pet groomer. Today, her task was trimming the four nails on dogs’ paws. She trimmed 164 nails, but three of the dogs had only three legs. How many dogs did Carly work on?"""
    total_nails = 164
    nails_per_dog = 4
    dogs_with_three_legs = 3
    total_dogs = (total_nails // nails_per_dog) + dogs_with_three_legs
    result = total_dogs
    return result

print(solution())