def solution():
    original_contents = 220  # The barrel originally had 220 liters of content
    loss_percentage = 0.1  # The barrel lost 10% of its contents
    loss_volume = original_contents * loss_percentage  # Calculate the volume of lost contents
    remaining_contents = original_contents - loss_volume  # Calculate the remaining contents
    result = remaining_contents
    return result

print(solution())