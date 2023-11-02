def solution():
    """Jana is 5 inches taller than Kelly, and Kelly is 3 inches shorter than Jess. If Jess is 72 inches tall, how tall is Jana?"""
    jess_height = 72
    kelly_height = jess_height - 3
    jana_height = kelly_height + 5
    result = jana_height
    return result

print(solution())