def solution():
    """Stefan, Vail, and Aiguo collected seashells. Stefan had 16 more seashells than Vail. Vail had 5 less than Aiguo. Aiguo had 20 seashells. How many seashells did the 3 children have in total?"""
    # Define Aiguo's number of seashells
    aiguo_seashells = 20

    # Calculate Vail's number of seashells
    vail_seashells = aiguo_seashells - 5

    # Calculate Stefan's number of seashells
    stefan_seashells = vail_seashells + 16

    # Calculate the total number of seashells collected
    total_seashells = aiguo_seashells + vail_seashells + stefan_seashells

    # Return the result
    result = total_seashells
    return result

print(solution())