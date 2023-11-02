def solution():
    """Carmen is preparing dinner plates for a row of customers at the counter in a diner. She likes to put a couple of sprigs of parsley on each plate for decoration. However, she is very low on parsley and doesn't have enough to even put 1 sprig on every plate, so she needs to break several of the parsley sprigs in two to make 2 smaller ones to stretch them out. If she decorates 8 plates with one whole parsley sprig and 12 plates with 1/2 a sprig each, how many sprigs of parsley does she have left if she started with 25?"""
    # Define the total number of parsley sprigs
    total_parsley_sprigs = 25

    # Calculate the number of parsley sprigs used for the plates with one whole sprig
    whole_sprig_plates = 8
    whole_sprig_parsley = whole_sprig_plates * 2

    # Calculate the number of parsley sprigs used for the plates with half a sprig
    half_sprig_plates = 12
    half_sprig_parsley = half_sprig_plates

    # Calculate the total number of parsley sprigs used
    total_used_parsley = whole_sprig_parsley + half_sprig_parsley

    # Calculate the number of parsley sprigs left
    parsley_left = total_parsley_sprigs - total_used_parsley

    # return the result
    result = parsley_left
    return result

print(solution())