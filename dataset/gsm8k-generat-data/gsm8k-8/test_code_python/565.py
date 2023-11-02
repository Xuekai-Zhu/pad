def solution():
    # Define the variables
    total_distance = 1000
    tracy_drive = 0
    michelle_drive = 0
    kati_drive = 0

    # Calculate Kati's driving distance
    kati_drive = total_distance / 10

    # Calculate Michelle's driving distance based on Kati's distance
    michelle_drive = 3 * kati_drive

    # Calculate Tracy's driving distance based on Michelle's distance
    tracy_drive = 20 + 2 * michelle_drive

    result = michelle_drive
    return result

print(solution())