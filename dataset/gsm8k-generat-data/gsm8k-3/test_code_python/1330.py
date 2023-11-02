def solution():
    """Sara is 6 inches taller than her brother Joe. Joe is 3 inches taller than his friend Roy. If Roy is 36 inches tall, how tall is Sara?"""
    # Define Roy's height
    ROY_HEIGHT = 36

    # Calculate Joe's height
    joe_height = ROY_HEIGHT + 3

    # Calculate Sara's height
    sara_height = joe_height + 6

    # Display Sara's height
    result = sara_height
    return result

print(solution())