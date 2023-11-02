def solution():
    CSA_uniform_color = "cadet gray"
    WP_uniform_color = "cadet gray and white"
    CSA_uniform_style = "single breasted jacket with button front and hat"
    WP_uniform_style = "standing collar, white trousers, and black shakos"
    if CSA_uniform_color in WP_uniform_color or CSA_uniform_style in WP_uniform_style:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())