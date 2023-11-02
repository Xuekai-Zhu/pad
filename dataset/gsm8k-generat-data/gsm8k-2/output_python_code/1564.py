def solution():
    """Jane is painting her fingernails. She applies a base coat that takes 2 minutes to dry, two color coats that take 3 minutes each to dry, and a clear topcoat that takes 5 minutes to dry. How many minutes total does Jane spend waiting for her nail polish to dry?"""
    base_coat_time = 2
    color_coat_time = 3
    top_coat_time = 5
    total_dry_time = base_coat_time + (2*color_coat_time) + top_coat_time
    result = total_dry_time
    return result

print(solution())