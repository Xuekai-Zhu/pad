def solution():
    whites_wash = 72
    whites_dry = 50

    darks_wash = 58
    darks_dry = 65

    colors_wash = 45
    colors_dry = 54

    # Calculate the total time for washing all loads
    total_wash_time = whites_wash + darks_wash + colors_wash

    # Calculate the total time for drying all loads
    total_dry_time = whites_dry + darks_dry + colors_dry

    # Calculate the total time for washing and drying all loads
    total_time = total_wash_time + total_dry_time
    result = total_time
    return result

print(solution())