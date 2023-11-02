def solution():
    total_size = 2300
    common_area = 1000
    guest_bedroom_size = 0.25 * master_bedroom_size

    # Calculate the total size of the remaining two bedrooms
    total_bedroom_size = total_size - common_area - guest_bedroom_size

    # Calculate the size of the master bedroom suite
    master_bedroom_size = total_bedroom_size / 1.25
    result = master_bedroom_size
    return result

print(solution())