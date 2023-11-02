def solution():
    """In a zoo, a hare is 14 inches tall, while a camel is 24 times taller than the hare. How tall is the camel in feet?"""
    hare_height_in = 14
    camel_height_in = hare_height_in * 24
    camel_height_ft = camel_height_in / 12
    result = camel_height_ft
    return result

print(solution())