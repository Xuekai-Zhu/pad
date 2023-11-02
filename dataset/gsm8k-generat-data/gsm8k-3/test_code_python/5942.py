def solution():
    """Tyrah has six times as many pencils as Sarah has. Tim has eight times as many pencils as Sarah. If Tyrah has 12 pencils, how many does Tim have?"""
    # Define the number of pencils Tyrah has and the ratio of pencils between Tyrah and Sarah
    tyrah_pencils = 12
    tyrah_to_sarah_ratio = 6

    # Calculate the number of pencils Sarah has
    sarah_pencils = tyrah_pencils / tyrah_to_sarah_ratio

    # Calculate the number of pencils Tim has
    tim_pencils = sarah_pencils * 8

    # Display the number of pencils Tim has
    result = tim_pencils
    return result

print(solution())