def solution():
    """A portable battery charger can fully charge a smartphone in 26 minutes or a tablet in 53 minutes. Ana charged her tablet fully and her phone halfway. How many minutes did it take?"""
    # Define the time to charge each device fully
    PHONE_TIME = 26
    TABLET_TIME = 53

    # Calculate the time it takes to charge Ana's tablet fully
    tablet_time = TABLET_TIME

    # Calculate the time it takes to charge Ana's phone halfway
    phone_time = PHONE_TIME / 2

    # Calculate the total time it takes to charge both devices
    total_time = tablet_time + phone_time

    # Display the total time
    result = total_time
    return result

print(solution())