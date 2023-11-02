def solution():
    """Charley bought 30 pencils. She lost 6 pencils while moving to school, and of course, also lost 1/3 of the remaining pencils because she wasn't very good at keeping track of pencils. How many pencils does she currently have?"""
    # Define the initial number of pencils
    initial_pencils = 30

    # Define the number of pencils lost while moving to school
    lost_pencils_1 = 6

    # Calculate the number of pencils remaining after the first loss
    remaining_pencils_1 = initial_pencils - lost_pencils_1

    # Define the fraction of pencils lost due to poor pencil-keeping
    loss_fraction = 1/3

    # Calculate the number of pencils lost due to poor pencil-keeping
    lost_pencils_2 = remaining_pencils_1 * loss_fraction

    # Calculate the number of pencils currently owned by Charley
    current_pencils = remaining_pencils_1 - lost_pencils_2

    # return the result
    result = current_pencils
    return result

print(solution())