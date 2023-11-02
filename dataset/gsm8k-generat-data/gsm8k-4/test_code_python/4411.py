def solution():
    """Alexis can sew a skirt in 2 hours and a coat in 7 hours. How long does it take for Alexis to sew 6 skirts and 4 coats?"""
    # Define the time it takes to sew a skirt and a coat
    skirt_time = 2
    coat_time = 7

    # Calculate the total time to sew 6 skirts and 4 coats
    total_skirt_time = 6 * skirt_time
    total_coat_time = 4 * coat_time
    total_time = total_skirt_time + total_coat_time

    # Return the result
    result = total_time
    return result

print(solution())