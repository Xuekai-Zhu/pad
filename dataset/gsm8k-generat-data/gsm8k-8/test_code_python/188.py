def solution():
    # Define the number of glasses David broke
    david_glasses_broken = 2

    # Define the number of glasses William broke
    william_glasses_broken = 4 * david_glasses_broken

    # Calculate the total number of glasses broken
    total_glasses_broken = david_glasses_broken + william_glasses_broken
    result = total_glasses_broken
    return result

print(solution())