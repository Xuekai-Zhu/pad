def solution():
    # Calculate the number of fake purses and handbags
    fake_purses = 26 / 2
    fake_handbags = 24 / 4

    # Calculate the number of authentic purses and handbags
    authentic_purses = 26 - fake_purses
    authentic_handbags = 24 - fake_handbags

    # Calculate the total number of genuine purses and handbags
    total_genuine = authentic_purses + authentic_handbags
    result = total_genuine
    return result

print(solution())