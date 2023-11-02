def solution():
    """Carolyn wants to embroider her new jeans. She can sew 4 stitches/minute. A flower takes 60 stitches to embroider, a unicorn takes 180 stitches, and Godzilla takes 800 stitches. If Carolyn wants to embroider Godzilla crushing 3 unicorns and 50 flowers, how many minutes does she need to spend embroidering?"""
    flower_stitches = 60
    unicorn_stitches = 180
    godzilla_stitches = 800
    flowers = 50
    unicorns = 3
    total_stitches = (flowers * flower_stitches) + (unicorns * unicorn_stitches) + godzilla_stitches
    embroidery_speed = 4
    total_time = total_stitches / embroidery_speed
    result = total_time
    return result

print(solution())