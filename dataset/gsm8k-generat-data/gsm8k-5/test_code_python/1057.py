def solution():
    total_gallons = 20  # 20 gallons of tea were poured
    num_containers = 80  # The tea was poured into 80 containers
    gallons_per_container = total_gallons / num_containers  # Calculate how many gallons are in each container

    # Calculate how many pints of tea Geraldo drank
    pints_drank = 3.5 * gallons_per_container * 8

    result = pints_drank
    return result

print(solution())