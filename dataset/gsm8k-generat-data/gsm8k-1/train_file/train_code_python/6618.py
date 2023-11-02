def solution():
    """A hurricane is approaching the southern coast of Texas, and a rancher is planning to move 400 head of cattle 60 miles to higher ground to protect them from possible inland flooding that might occur. His animal transport truck holds 20 head of cattle. Traveling at 60 miles per hour, what is the total driving time, in hours, it will take to transport all of his cattle to higher ground?"""
    total_cattle = 400
    capacity_per_truck = 20
    trucks_needed = total_cattle // capacity_per_truck + (total_cattle % capacity_per_truck > 0)
    distance = 60
    speed = 60
    time = distance / speed
    total_time = time * trucks_needed
    result = total_time
    return result

print(solution())