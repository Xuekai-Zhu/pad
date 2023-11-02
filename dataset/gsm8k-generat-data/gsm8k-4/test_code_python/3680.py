def solution():
    """Tirzah has a lot of purses and handbags; in total she has 26 purses and 24 handbags. Half the purses and 1/4 the handbags are fake. If the rest are authentic, how many purses and handbags in total are genuine?"""
    # Calculate the number of fake purses
    fake_purses = 26 * 0.5

    # Calculate the number of genuine purses
    genuine_purses = 26 - fake_purses

    # Calculate the number of fake handbags
    fake_handbags = 24 * 0.25

    # Calculate the number of genuine handbags
    genuine_handbags = 24 - fake_handbags

    # Calculate the total number of genuine purses and handbags
    total_genuine = genuine_purses + genuine_handbags

    # Display the result
    result = total_genuine
    return result

print(solution())