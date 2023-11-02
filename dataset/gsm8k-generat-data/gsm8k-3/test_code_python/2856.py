def solution():
    """Mary is going on a business trip. It takes 10 minutes for her Uber to get to her house and 5 times longer to get to the airport. It takes 15 minutes to check her bag and three times as long to get through security. Then she has to wait for 20 minutes for her flight to start boarding and twice as long before the plane is ready to take off. How many hours will this process take total?"""
    # Convert all time values to hours
    ubertohome = 10 / 60
    hometoairport = ubertohome * 5
    checkbag = 15 / 60
    security = checkbag * 3
    waittoboard = 20 / 60
    waittotakeoff = waittoboard * 2

    # Calculate the total time
    total_time = ubertohome + hometoairport + checkbag + security + waittoboard + waittotakeoff

    # Display the total time in hours
    result = total_time
    return result

print(solution())