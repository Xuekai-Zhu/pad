def solution():
    """Telegraph Road goes through multiple states and is 162 kilometers long. Pardee Road is 12000 meters long. How many kilometers longer is Telegraph Road than Pardee Road?"""
    # Convert Pardee Road length to kilometers
    pardee_length = 12000 / 1000

    # Calculate the difference in length between Telegraph Road and Pardee Road
    length_diff = 162 - pardee_length

    # Display the length difference in kilometers
    result = length_diff
    return result

print(solution())