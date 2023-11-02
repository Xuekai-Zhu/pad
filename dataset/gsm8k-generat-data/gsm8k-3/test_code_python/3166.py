def solution():
    """Louise is hanging 30 of her pictures on the wall. She hangs some of them vertically, half of them horizontally, then hangs the remaining 5 pictures haphazardly. How many pictures did Louise hang vertically?"""
    # Define the total number of pictures
    total_pictures = 30

    # Calculate the number of pictures hung horizontally
    horizontal_pictures = total_pictures // 2

    # Calculate the number of pictures hung haphazardly
    haphazard_pictures = 5

    # Calculate the number of pictures hung vertically
    vertical_pictures = total_pictures - horizontal_pictures - haphazard_pictures

    # Display the number of pictures hung vertically
    result = vertical_pictures
    return result

print(solution())