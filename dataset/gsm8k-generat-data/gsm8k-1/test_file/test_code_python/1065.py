def solution():
    """
    Mr Hezekiah had 20 trucks from his store supplying fertiliser to different farmers in his hometown dispatched for delivery on a particular day.
    Each truck was carrying 20 tons of fertiliser packed in bags.
    Two hours after the trucks had departed for delivery, Mr Hezekiah got the news that a quarter of the number of lorries dispatched for delivery had mechanical failures on the road and could not deliver the fertilisers to the farmers.
    Calculate the total number of tons of fertiliser that reached the farmers that day?
    """
    num_trucks = 20
    tons_per_truck = 20
    num_failed_trucks = num_trucks / 4
    num_delivered_trucks = num_trucks - num_failed_trucks
    tons_delivered = num_delivered_trucks * tons_per_truck
    result = tons_delivered
    return result

print(solution())