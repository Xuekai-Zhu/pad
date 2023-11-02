def solution():
    # Calculate the percentage of mornings Jake trips over his dog
    percent_trips = 40

    # Calculate the percentage of times he drops his coffee when he trips
    percent_drops = 25

    # Calculate the percentage of mornings he doesn't drop his coffee
    percent_no_drop = 100 - (percent_trips * percent_drops / 100)

    result = percent_no_drop
    return result

print(solution())