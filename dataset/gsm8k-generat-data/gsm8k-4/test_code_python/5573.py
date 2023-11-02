def solution():
    """Amy bakes muffins for her friends. On Monday, she brings 1 muffin to school to share. Each day for the rest of the week she brings one more muffin to school than she did the day before. If on Saturday she counts that there are 7 muffins left, how many did she originally bake?"""
    # Define the number of muffins Amy brought to school on Monday
    monday_muffins = 1

    # Calculate the total number of muffins Amy brought to school during the week
    total_muffins = monday_muffins + (monday_muffins + 1) + (monday_muffins + 2) + (monday_muffins + 3) + (monday_muffins + 4)

    # Calculate the number of muffins Amy originally baked by adding the 7 she has left on Saturday
    original_bake = total_muffins + 7

    # Return the result
    result = original_bake
    return result

print(solution())