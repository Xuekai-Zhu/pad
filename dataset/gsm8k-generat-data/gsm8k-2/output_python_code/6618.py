def solution():
    """A hurricane is approaching the southern coast of Texas, and a rancher is planning to move 400 head of cattle 60 miles to higher ground to protect them from possible inland flooding that might occur. His animal transport truck holds 20 head of cattle. Traveling at 60 miles per hour, what is the total driving time, in hours, it will take to transport all of his cattle to higher ground?"""
    cattle_count = 400
    transport_capacity = 20
    distance = 60
    speed = 60
    trips_required = cattle_count // transport_capacity
    if cattle_count % transport_capacity != 0:
        trips_required += 1

    total_distance = distance * trips_required
    total_time = total_distance / speed
    result = total_time
    return result

print(solution())