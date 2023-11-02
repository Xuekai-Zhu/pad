def solution():
    """Jake sold 10 more stuffed animals than Thor. Quincy sold ten times as many stuffed animals as Thor. If Quincy sold 200 stuffed animals, how many more stuffed animals did Quincy sell than Jake?"""
    # Calculate how many stuffed animals Thor sold
    thor_sold = (200 / 10)  # Quincy sold ten times as many stuffed animals as Thor

    # Calculate how many stuffed animals Jake sold
    jake_sold = thor_sold + 10  # Jake sold 10 more stuffed animals than Thor

    # Calculate how many more stuffed animals Quincy sold than Jake
    quincy_extra = 200 - (thor_sold + jake_sold)

    # Display the result
    result = quincy_extra
    return result

print(solution())