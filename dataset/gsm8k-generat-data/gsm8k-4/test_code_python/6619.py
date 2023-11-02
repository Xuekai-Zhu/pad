def solution():
    """A hurricane is approaching the southern coast of Texas, and a rancher is planning to move 400 head of cattle 60 miles to higher ground to protect them from possible inland flooding that might occur. His animal transport truck holds 20 head of cattle. Traveling at 60 miles per hour, what is the total driving time, in hours, it will take to transport all of his cattle to higher ground?"""
    # Define the number of cattle and the capacity of the transport truck
    cattle = 400
    truck_capacity = 20

    # Calculate the number of trips the rancher needs to make
    trips = cattle // truck_capacity
    if cattle % truck_capacity != 0:
        trips += 1

    # Calculate the total distance that needs to be traveled
    distance = trips * 60

    # Calculate the total driving time
    time = distance / 60

    result = time
    return result

print(solution())