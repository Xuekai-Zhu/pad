def solution():
    aiguo_seashells = 20  # Aiguo had 20 seashells
    vail_seashells = aiguo_seashells - 5  # Vail had 5 less than Aiguo
    stefan_seashells = vail_seashells + 16  # Stefan had 16 more than Vail

    # Calculate the total number of seashells collected by the three children
    total_seashells = aiguo_seashells + vail_seashells + stefan_seashells
    result = total_seashells
    return result

print(solution())