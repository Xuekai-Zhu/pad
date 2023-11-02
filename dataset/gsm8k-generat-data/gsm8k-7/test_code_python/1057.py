def solution():
    num_gallons = 20
    num_containers = 80
    num_drunk_containers = 3.5

    # Calculate the total number of pints of tea
    total_pints = num_gallons * 8 * 4

    # Calculate the number of pints in one container
    pints_per_container = total_pints / num_containers

    # Calculate the total number of pints drunk by Geraldo
    total_drunk_pints = num_drunk_containers * pints_per_container
    result = total_drunk_pints
    return result

print(solution())