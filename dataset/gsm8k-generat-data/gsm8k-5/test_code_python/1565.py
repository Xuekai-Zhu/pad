def solution():
    base_coat_time = 2  # Base coat takes 2 minutes to dry
    color_coat_time = 3  # Each color coat takes 3 minutes to dry
    top_coat_time = 5  # Top coat takes 5 minutes to dry

    # Calculate the total time waiting for nail polish to dry
    total_time = base_coat_time + (2 * color_coat_time) + top_coat_time
    result = total_time
    return result

print(solution())