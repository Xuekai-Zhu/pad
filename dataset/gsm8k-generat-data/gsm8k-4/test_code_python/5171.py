def solution():
    """Abby is building 2 raised beds to grow vegetables. The beds are both 8 feet long, 4 feet wide and 1 foot high. Each bag of soil has 4 cubic feet. How many bags of soil will she need?"""
    # Define the dimensions of each raised bed
    length = 8
    width = 4
    height = 1

    # Calculate the volume of each raised bed
    volume = length * width * height

    # Calculate the total volume of soil needed for both raised beds
    total_volume = volume * 2

    # Calculate the number of bags of soil needed
    bags = total_volume / 4

    result = bags
    return result

print(solution())