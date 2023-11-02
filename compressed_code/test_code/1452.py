def solution():
    
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