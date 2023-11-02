def solution():
    """Carmen is preparing dinner plates for a row of customers at the counter in a diner. She likes to put a couple of sprigs of parsley on each plate for decoration. However, she is very low on parsley and doesn't have enough to even put 1 sprig on every plate, so she needs to break several of the parsley sprigs in two to make 2 smaller ones to stretch them out. If she decorates 8 plates with one whole parsley sprig and 12 plates with 1/2 a sprig each, how many sprigs of parsley does she have left if she started with 25?"""
    # Define the number of plates to decorate with a whole parsley sprig and half a sprig
    WHOLE_PLATES = 8
    HALF_PLATES = 12

    # Calculate the total number of parsley sprigs used
    total_sprigs = WHOLE_PLATES + HALF_PLATES * 0.5

    # Calculate the number of parsley sprigs left
    sprigs_left = 25 - total_sprigs

    # Display the number of parsley sprigs left
    result = sprigs_left
    return result

print(solution())