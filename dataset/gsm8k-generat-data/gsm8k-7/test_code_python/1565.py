def solution():
    base_coat_dry_time = 2
    color_coat_dry_time = 3
    num_color_coats = 2
    top_coat_dry_time = 5

    # Calculate the total dry time for the color coats
    total_color_coat_dry_time = color_coat_dry_time * num_color_coats

    # Calculate the total time spent waiting for nail polish to dry
    total_dry_time = base_coat_dry_time + total_color_coat_dry_time + top_coat_dry_time
    result = total_dry_time
    return result

print(solution())