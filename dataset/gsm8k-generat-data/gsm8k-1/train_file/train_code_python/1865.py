def solution():
    """Carolyn wants to embroider her new jeans. She can sew 4 stitches/minute. A flower takes 60 stitches to embroider, a unicorn takes 180 stitches, and Godzilla takes 800 stitches. If Carolyn wants to embroider Godzilla crushing 3 unicorns and 50 flowers, how many minutes does she need to spend embroidering?"""
    stitches_per_minute = 4
    flower_stitches = 60
    unicorn_stitches = 180
    godzilla_stitches = 800
    total_stitches = (godzilla_stitches + (3*unicorn_stitches) + (50*flower_stitches))
    time_required = total_stitches / stitches_per_minute
    result = time_required
    return result

print(solution())