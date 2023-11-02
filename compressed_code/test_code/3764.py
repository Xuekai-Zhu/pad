def solution():
    
    hat_time = 2
    scarf_time = 3
    mitten_time = 1
    sock_time = 1.5
    sweater_time = 6
    num_outfits = 3

    total_time = (hat_time + scarf_time + (2 * mitten_time) + (2 * sock_time) + sweater_time) * num_outfits
    result = total_time
    return result

print(solution())