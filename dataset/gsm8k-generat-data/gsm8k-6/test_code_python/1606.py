def solution():
    # Calculate Maya's initial lifting capacity and final peak lifting capacity
    initial_lift = 240 / 4  # Maya can lift a fourth of what America can
    peak_lift = 300 / 2  # Maya reaches her absolute peak and can lift half of what America can lift

    # Calculate the difference in Maya's lifting capacity from start to peak
    difference = peak_lift - initial_lift

    # Calculate how much more Maya can lift now than when she started
    additional_lift = (peak_lift - initial_lift) - (peak_lift - (initial_lift + 10))

    result = additional_lift
    return result

print(solution())