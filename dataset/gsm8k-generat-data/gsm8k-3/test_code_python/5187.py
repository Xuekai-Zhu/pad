def solution():
    """There are 7 mL of solution in each of 6 test tubes. Dr. Igor takes all of the solution and then evenly distributes it into 3 beakers. How many mL of solution are in each beaker?"""
    # Define the number of test tubes and the volume of solution in each
    num_tubes = 6
    tube_volume = 7

    # Calculate the total volume of solution
    total_volume = num_tubes * tube_volume

    # Calculate the volume of solution in each beaker
    beaker_volume = total_volume / 3

    # Display the volume of solution in each beaker
    result = beaker_volume
    return result

print(solution())