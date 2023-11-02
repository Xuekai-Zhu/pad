def solution():
    """Sally picks 30 seashells on Monday. On Tuesday, she picks half as many seashells as she did on Monday. If she can sell each seashell for $1.20, how much money can she make if she sells all of her seashells?"""
    # Define the number of seashells Sally picked on Monday
    monday_seashells = 30

    # Calculate the number of seashells Sally picked on Tuesday
    tuesday_seashells = monday_seashells / 2

    # Calculate the total number of seashells Sally picked
    total_seashells = monday_seashells + tuesday_seashells

    # Calculate Sally's total earnings from selling the seashells
    earnings = total_seashells * 1.20

    # Display Sally's total earnings
    result = earnings
    return result

print(solution())