def solution():
    pictures_randy = 5  # Randy drew 5 pictures
    pictures_peter = pictures_randy + 3  # Peter drew 3 more pictures than Randy
    pictures_quincy = pictures_peter + 20  # Quincy drew 20 more pictures than Peter

    # Calculate the total number of pictures drawn altogether
    total_pictures = pictures_randy + pictures_peter + pictures_quincy
    result = total_pictures
    return result

print(solution())