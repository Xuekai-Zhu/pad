def solution():
    # Find the number of hikes Amanda and Steven have gone on
    hikes_amanda = 8 * 7  # Amanda has gone on 8 times more hikes than Camila
    hikes_steven = hikes_amanda + 15  # Steven has gone on 15 more hikes than Amanda

    # Calculate the number of hikes Camila needs to go on to catch up to Steven
    hikes_needed = hikes_steven - 7  # Camila needs to have hiked as many times as Steven

    # Calculate the number of weeks it will take Camila to achieve her goal
    weeks_needed = hikes_needed / 4  # Assuming 4 hikes per week
    result = weeks_needed
    return result

print(solution())