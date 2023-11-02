def solution():
    """Three frogs are trying to hop across the road. The first frog takes 4 times as many hops as the second. The second frog takes twice as many as the third. If the three frogs took a total of 99 hops, how many hops did it take the second frog to cross the road?"""
    # Define the number of hops taken by the third frog
    third_frog_hops = x

    # Define the number of hops taken by the second frog
    second_frog_hops = 2 * third_frog_hops

    # Define the number of hops taken by the first frog
    first_frog_hops = 4 * second_frog_hops

    # Calculate the total number of hops taken
    total_hops = first_frog_hops + second_frog_hops + third_frog_hops

    # Solve for x using the equation total_hops = 99
    x = (99 - (4 + 2 + 1) * x) / 7

    # Calculate the number of hops taken by the second frog
    second_frog_hops = 2 * x

    # Return the result
    result = second_frog_hops
    return result

print(solution())