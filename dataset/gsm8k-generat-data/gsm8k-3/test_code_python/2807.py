def solution():
    """Osborn is testing a new way to get dressed in the morning on school days so he goes faster and can get up later. He tracks his time for the week and on Monday is takes him 2 minutes. On Tuesday it takes him 4 minutes. On Wednesday it takes him 3 minutes. On Thursday it takes him 4 minutes. Before Friday arrives he looks at his old way of getting dressed and sees that it was taking him 3 minutes on average to get dressed. How fast does he have to get dressed on Friday so his weekly average ties his old method?"""
    # Calculate the total minutes spent getting dressed from Monday to Thursday
    total_time = 2 + 4 + 3 + 4

    # Calculate the time Osborn needs to spend on Friday to get the weekly average of 3 minutes
    friday_time = (5 * 3) - total_time

    # Display the time Osborn needs to spend on Friday
    result = friday_time
    return result

print(solution())