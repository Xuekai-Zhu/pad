def solution():
    """Toby, the Alaskan Malamute, can pull a sled at a speed of 20 miles per hour if the sled is unloaded, but he pulls the same sled at a speed of 10 miles per hour if the sled is fully loaded.  If Toby takes a continuous 4-part journey, first pulling the loaded sled for 180 miles, then pulling the unloaded sled for 120 miles, then pulling the loaded sled 80 miles, and finally, pulling the unloaded sled another 140 miles, how many hours in total will Toby spend pulling the sled?"""
    # Define Toby's unloaded and loaded speed
    UNLOADED_SPEED = 20
    LOADED_SPEED = 10

    # Calculate the time taken for each leg of the journey
    time1 = 180 / LOADED_SPEED
    time2 = 120 / UNLOADED_SPEED
    time3 = 80 / LOADED_SPEED
    time4 = 140 / UNLOADED_SPEED

    # Calculate the total time taken
    total_time = time1 + time2 + time3 + time4

    # Display the total time taken
    result = total_time
    return result

print(solution())