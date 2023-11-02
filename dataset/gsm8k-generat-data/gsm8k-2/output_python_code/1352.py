def solution():
    """In a zoo, a hare is 14 inches tall, while a camel is 24 times taller than the hare. How tall is the camel in feet?"""
    hare_height = 14
    camel_height = 24 * hare_height
    camel_height_feet = camel_height / 12
    result = camel_height_feet
    return result

print(solution())