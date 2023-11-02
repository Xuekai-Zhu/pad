def solution():
    # Define the top speed of the Chicago "L" and the fastest tortoise's average speed
    l_train_top_speed = 55
    tortoise_speed = 0.63
    # Convert the L train's top speed to miles per hour
    l_train_top_speed_mph = l_train_top_speed * 0.621371
    # Compare the speeds and determine if the tortoise would win
    if tortoise_speed > l_train_top_speed_mph:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())