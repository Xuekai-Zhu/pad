def solution():
    # Define the number of pictures Peter and Quincy drew
    peter_pictures = 8
    quincy_pictures = peter_pictures + 20

    # Calculate the number of pictures Randy drew
    randy_pictures = 41 - (peter_pictures + quincy_pictures)
    result = randy_pictures
    return result

print(solution())