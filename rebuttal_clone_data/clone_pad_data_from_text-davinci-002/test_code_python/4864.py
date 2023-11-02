def solution():
    hats = 3
    time_to_knit_hat = 2
    scarves = 3
    time_to_knit_scarf = 3
    mittens = 3
    time_to_knit_mittens = 1
    socks = 3
    time_to_knit_socks = 1.5
    sweaters = 3
    time_to_knit_sweater = 6
    
    total_time = hats * time_to_knit_hat + scarves * time_to_knit_scarf + mittens * time_to_knit_mittens + socks * time_to_knit_socks + sweaters * time_to_knit_sweater
    result = total_time
    return result

print(solution())