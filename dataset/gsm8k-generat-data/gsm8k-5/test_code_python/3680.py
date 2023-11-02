def solution():
    # Calculate the number of fake purses
    fake_purses = 0.5 * 26

    # Calculate the number of fake handbags
    fake_handbags = 0.25 * 24

    # Calculate the number of authentic purses and handbags
    authentic_purses = 26 - fake_purses
    authentic_handbags = 24 - fake_handbags

    # Calculate the total number of genuine purses and handbags
    genuine_total = authentic_purses + authentic_handbags
    result = genuine_total
    return result

print(solution())