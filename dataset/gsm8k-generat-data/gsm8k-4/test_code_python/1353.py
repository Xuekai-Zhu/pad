def solution():
    """In a zoo, a hare is 14 inches tall, while a camel is 24 times taller than the hare. How tall is the camel in feet?"""
    # Define the height of the hare in inches
    hare_height_inches = 14

    # Calculate the height of the camel in inches
    camel_height_inches = hare_height_inches * 24

    # Convert the height of the camel from inches to feet
    camel_height_feet = camel_height_inches / 12

    # return the result
    result = camel_height_feet
    return result

print(solution())