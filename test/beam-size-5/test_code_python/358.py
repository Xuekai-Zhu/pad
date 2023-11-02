def solution():
    
    # Define the stuffing required for each type of bed
    ROTTWEiler_STUDENTING = 8
    CHIHUAHUA_STUDENTING = 2
    COLLIE_STUDENTING = (4 * CHIHUAHUA_STUDENTING) + (3 * COLLIE_STUDENTING)

    # Calculate the total stuffing required
    total_stuffing = ROTTWEiler_STUDENTING + CHIHUAHUA_STUDENTING + COLLIE_STUDENTING

    # Display the total stuffing required
    result = total_stuffing
    return result

print(solution())