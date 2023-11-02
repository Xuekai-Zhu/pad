def solution():
    """Carolyn wants to embroider her new jeans. She can sew 4 stitches/minute. A flower takes 60 stitches to embroider, a unicorn takes 180 stitches, and Godzilla takes 800 stitches. If Carolyn wants to embroider Godzilla crushing 3 unicorns and 50 flowers, how many minutes does she need to spend embroidering?"""
    # Define the number of stitches for each item
    FLOWER_STITCHES = 60
    UNICORN_STITCHES = 180
    GODZILLA_STITCHES = 800

    # Define the number of each item Carolyn wants to embroider
    flower_count = 50
    unicorn_count = 3
    godzilla_count = 1

    # Calculate the total number of stitches Carolyn needs to embroider
    total_stitches = (flower_count * FLOWER_STITCHES) + (unicorn_count * UNICORN_STITCHES) + (godzilla_count * GODZILLA_STITCHES)

    # Calculate the time Carolyn needs to spend embroidering
    time_minutes = total_stitches / 4

    # Display the time Carolyn needs to spend embroidering
    result = time_minutes
    return result

print(solution())