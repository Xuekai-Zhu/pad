def solution():
    """Stefan, Vail, and Aiguo collected seashells. Stefan had 16 more seashells than Vail. Vail had 5 less than Aiguo. Aiguo had 20 seashells. How many seashells did the 3 children have in total?"""
    # Define the number of seashells Aiguo had
    aiguo_seashells = 20

    # Determine the number of seashells Vail had
    vail_seashells = aiguo_seashells - 5

    # Determine the number of seashells Stefan had
    stefan_seashells = vail_seashells + 16

    # Calculate the total number of seashells collected
    total_seashells = aiguo_seashells + vail_seashells + stefan_seashells

    # Display the total number of seashells collected
    result = total_seashells
    return result

print(solution())