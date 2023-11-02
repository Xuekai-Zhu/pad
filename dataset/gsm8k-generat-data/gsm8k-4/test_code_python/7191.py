def solution():
    """Sally picks 30 seashells on Monday. On Tuesday, she picks half as many seashells as she did on Monday. If she can sell each seashell for $1.20, how much money can she make if she sells all of her seashells?"""
    # Define the number of seashells picked on Monday
    monday_seashells = 30

    # Calculate the number of seashells picked on Tuesday
    tuesday_seashells = monday_seashells / 2

    # Calculate the total number of seashells picked
    total_seashells = monday_seashells + tuesday_seashells

    # Calculate the total earnings from selling seashells
    earnings = total_seashells * 1.20

    result = earnings
    return result

print(solution())