def solution():
    """Carly is a pet groomer. Today, her task was trimming the four nails on dogs’ paws. She trimmed 164 nails, but three of the dogs had only three legs. How many dogs did Carly work on?"""
    # Calculate the number of nails on dogs with 4 legs
    nails_4_legs = (164 // 4) * 4

    # Calculate the number of nails on dogs with 3 legs
    nails_3_legs = (164 - nails_4_legs) // 3 * 3

    # Calculate the total number of dogs worked on
    dogs_worked_on = (nails_4_legs + nails_3_legs) // 4

    # Display the total number of dogs worked on
    result = dogs_worked_on
    return result

print(solution())