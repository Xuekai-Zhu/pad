def solution():
    """Chuck can ride the merry-go-round 5 times longer than Dave who can only ride it for 10 minutes before getting sick.  Erica can stay on the merry-go-round 30% longer than Chuck before getting sick.  How long can Erica stay on the merry-go-round?"""
    # Define Dave's ride time and Chuck's ride time relative to Dave's
    DAVE_RIDE_TIME = 10
    CHUCK_RIDE_TIME = DAVE_RIDE_TIME * 5

    # Calculate Chuck's ride time in minutes and then Erica's ride time
    CHUCK_RIDE_TIME_MIN = CHUCK_RIDE_TIME * 60
    ERICA_RIDE_TIME_MIN = CHUCK_RIDE_TIME_MIN * 1.3

    # Convert Erica's ride time back to hours and minutes
    ERICA_RIDE_TIME_HR = ERICA_RIDE_TIME_MIN // 60
    ERICA_RIDE_TIME_MIN = ERICA_RIDE_TIME_MIN % 60

    # Display Erica's ride time
    result = f"{ERICA_RIDE_TIME_HR} hours and {ERICA_RIDE_TIME_MIN} minutes"
    return result

print(solution())