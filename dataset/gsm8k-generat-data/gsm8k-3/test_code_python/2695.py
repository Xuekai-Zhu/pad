def solution():
    """Marcus spends 20 minutes giving his dog a bath and half as long blow-drying her. Then he takes her for a walk along a 3-mile trail. If Marcus walks at 6 miles per hour, how much time does he spend with his dog total?"""
    # Convert 20 minutes to hours
    bath_time = 20 / 60

    # Calculate blow-dry time as half of bath time
    blow_dry_time = bath_time / 2

    # Calculate the time it takes to walk the 3-mile trail
    walk_time = 3 / 6

    # Calculate total time spent with the dog
    total_time = bath_time + blow_dry_time + walk_time

    # Display the total time spent with the dog
    result = total_time
    return result

print(solution())