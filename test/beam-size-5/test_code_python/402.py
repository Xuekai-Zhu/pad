def solution():
    
    # Define the number of cannolis and the ratio of corns to cannolis
    cannolis = 40
    corn_to_cannolis_ratio = 2

    # Calculate the number of cannolis Allan bought
    allan_cannolis = cannolis + 60

    # Calculate the number of corns Allan bought
    allan_corns = allan_cannolis - 40

    # Calculate the combined total of cannolis and corns
    total = allan_cannolis + allan_corns

    # Display the combined total
    result = total
    return result

print(solution())