def solution():
    # Calculate the number of seashells collected by Vail
    vail_seashells = 20 - 5  # Vail had 5 less than Aiguo

    # Calculate the number of seashells collected by Stefan
    stefan_seashells = vail_seashells + 16  # Stefan had 16 more seashells than Vail

    # Calculate the total number of seashells collected
    total_seashells = aiguo_seashells + vail_seashells + stefan_seashells
    result = total_seashells
    return result

print(solution())