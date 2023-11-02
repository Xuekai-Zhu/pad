def solution():
    """Carmen is preparing dinner plates for a row of customers at the counter in a diner. She likes to put a couple of sprigs of parsley on each plate for decoration. However, she is very low on parsley and doesn't have enough to even put 1 sprig on every plate, so she needs to break several of the parsley sprigs in two to make 2 smaller ones to stretch them out. If she decorates 8 plates with one whole parsley sprig and 12 plates with 1/2 a sprig each, how many sprigs of parsley does she have left if she started with 25?"""
    starting_sprigs = 25
    used_sprigs = 8 + 12 * 0.5
    remaining_sprigs = starting_sprigs - used_sprigs
    result = remaining_sprigs
    return result

print(solution())