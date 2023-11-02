def solution():
    """A hurricane is approaching the southern coast of Texas, and a rancher is planning to move 400 head of cattle 60 miles to higher ground to protect them from possible inland flooding that might occur.  His animal transport truck holds 20 head of cattle.  Traveling at 60 miles per hour, what is the total driving time, in hours, it will take to transport all of his cattle to higher ground?"""
    # Calculate the total number of trips needed
    num_trips = 400 // 20
    if 400 % 20 != 0:
        num_trips += 1

    # Calculate the total distance traveled
    total_distance = num_trips * 60

    # Calculate the total driving time
    driving_time = total_distance / 60

    # Display the total driving time
    result = driving_time
    return result

print(solution())