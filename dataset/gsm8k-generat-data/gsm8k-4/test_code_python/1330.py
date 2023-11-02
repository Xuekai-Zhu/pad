def solution():
    """Sara is 6 inches taller than her brother Joe. Joe is 3 inches taller than his friend Roy. If Roy is 36 inches tall, how tall is Sara?"""
    # Define the height of Roy
    roy_height = 36

    # Calculate the height of Joe
    joe_height = roy_height + 3

    # Calculate the height of Sara
    sara_height = joe_height + 6

    # return the result
    result = sara_height
    return result

print(solution())