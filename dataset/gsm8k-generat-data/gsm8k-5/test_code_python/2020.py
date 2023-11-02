def solution():
    oysters_per_time = 10  # Bob can shuck 10 oysters in 5 minutes
    time_in_minutes = 120  # Bob has 2 hours to shuck oysters

    # Calculate the total number of oysters Bob can shuck in 2 hours
    total_oysters = (oysters_per_time / 5) * time_in_minutes

    result = total_oysters
    return result

print(solution())