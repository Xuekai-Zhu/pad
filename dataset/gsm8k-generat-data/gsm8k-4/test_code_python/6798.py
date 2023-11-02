def solution():
    """Lena played video games for 3.5 hours last weekend. Her brother played 17 minutes more than she did. How many minutes together did Lena and her brother play video games last weekend?"""
    # Convert Lena's playtime to minutes
    lena_minutes = 3.5 * 60

    # Calculate her brother's playtime in minutes
    brother_minutes = lena_minutes + 17

    # Calculate the total playtime in minutes
    total_minutes = lena_minutes + brother_minutes

    result = total_minutes
    return result

print(solution())