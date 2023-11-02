def solution():
    """Carolyn wants to embroider her new jeans. She can sew 4 stitches/minute. A flower takes 60 stitches to embroider, a unicorn takes 180 stitches, and Godzilla takes 800 stitches. If Carolyn wants to embroider Godzilla crushing 3 unicorns and 50 flowers, how many minutes does she need to spend embroidering?"""
    # Define the number of stitches per minute and the number of stitches for each item
    STITCHES_PER_MINUTE = 4
    FLOWER_STITCHES = 60
    UNICORN_STITCHES = 180
    GODZILLA_STITCHES = 800

    # Calculate the total number of stitches Carolyn needs to embroider
    total_stitches = (3 * UNICORN_STITCHES) + (50 * FLOWER_STITCHES) + GODZILLA_STITCHES

    # Calculate the time Carolyn needs to spend embroidering
    time = total_stitches / STITCHES_PER_MINUTE

    # Return the result in minutes
    result = time
    return result

print(solution())