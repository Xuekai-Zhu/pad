def solution():
    # Define the time it takes to knit each item
    hat_time = 2
    scarf_time = 3
    mitten_time = 1
    sock_time = 1.5
    sweater_time = 6

    # Calculate the total time it takes to knit one outfit
    outfit_time = hat_time + scarf_time + (2 * mitten_time) + (2 * sock_time) + sweater_time

    # Calculate the total time it takes to knit all three outfits
    total_time = outfit_time * 3
    result = total_time
    return result

print(solution())