def solution():
    """Tirzah has a lot of purses and handbags; in total she has 26 purses and 24 handbags. Half the purses and 1/4 the handbags are fake. If the rest are authentic, how many purses and handbags in total are genuine?"""
    # Calculate the number of fake purses and handbags
    fake_purses = 26 * 0.5
    fake_handbags = 24 * 0.25

    # Calculate the number of genuine purses and handbags
    genuine_purses = 26 - fake_purses
    genuine_handbags = 24 - fake_handbags

    # Calculate the total number of genuine purses and handbags
    total_genuine = genuine_purses + genuine_handbags

    # Display the total number of genuine purses and handbags
    result = total_genuine
    return result

print(solution())