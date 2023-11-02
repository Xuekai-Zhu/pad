def solution():
    """Amy bakes muffins for her friends. On Monday, she brings 1 muffin to school to share. Each day for the rest of the week she brings one more muffin to school than she did the day before. If on Saturday she counts that there are 7 muffins left, how many did she originally bake?"""
    # Initialize the total number of muffins
    total_muffins = 0

    # Calculate the number of muffins brought each day
    for i in range(1, 7):
        total_muffins += i

    # Add the muffin brought on Monday
    total_muffins += 1

    # Subtract the muffins left on Saturday
    total_muffins -= 7

    # Display the originally baked muffins
    result = total_muffins
    return result

print(solution())