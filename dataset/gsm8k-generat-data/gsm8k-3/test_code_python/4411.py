def solution():
    """Alexis can sew a skirt in 2 hours and a coat in 7 hours. How long does it take for Alexis to sew 6 skirts and 4 coats?"""
    # Define the time it takes to sew one skirt and one coat
    SKIRT_TIME = 2
    COAT_TIME = 7

    # Calculate the total time it takes to sew 6 skirts
    total_skirt_time = SKIRT_TIME * 6

    # Calculate the total time it takes to sew 4 coats
    total_coat_time = COAT_TIME * 4

    # Calculate the total time it takes to sew all the clothing items
    total_time = total_skirt_time + total_coat_time

    # Display the total time
    result = total_time
    return result

print(solution())