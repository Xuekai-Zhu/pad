def solution():
    
    # Define the amount of stuffing needed for each type of bed
    ROTTWEILER_STUFFING = 8
    CHIHUAHUA_STUFFING = 2
    COLLIE_STUFFING = (ROTTWEILER_STUFFING + CHIHUAHUA_STUFFING) / 2

    # Define the number of each type of bed Mark needs to make
    num_chihuahua_beds = 4
    num_collie_beds = 3

    # Calculate the total amount of stuffing needed
    total_stuffing = (num_chihuahua_beds * CHIHUAHUA_STUFFING) + (num_collie_beds * COLLIE_STUFFING)

    # Display the total amount of stuffing needed
    result = total_stuffing
    return result

print(solution())