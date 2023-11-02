def solution():
    jenson_shirts_per_day = 3
    jenson_fabric_per_shirt = 2
    kingsley_pants_per_day = 5
    kingsley_fabric_per_pant = 5
    num_days = 3

    # Calculate the total number of yards of fabric Jenson uses per day
    jenson_fabric_per_day = jenson_shirts_per_day * jenson_fabric_per_shirt

    # Calculate the total number of yards of fabric Kingsley uses per day
    kingsley_fabric_per_day = kingsley_pants_per_day * kingsley_fabric_per_pant

    # Calculate the total number of yards of fabric used by both Jenson and Kingsley per day
    total_fabric_per_day = jenson_fabric_per_day + kingsley_fabric_per_day

    # Calculate the total number of yards of fabric used by both Jenson and Kingsley in 3 days
    total_fabric = total_fabric_per_day * num_days
    result = total_fabric
    return result

print(solution())