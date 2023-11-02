def solution():
    """There are 30 spaces for each vehicle in a parking lot. A caravan takes up a total of 2 spaces of parking space. How many vehicles can still park if there are 3 caravans currently parking?"""
    # Define the total number of parking spaces and the space taken up by a caravan
    total_spaces = 30
    caravan_space = 2

    # Calculate the total space taken up by the caravans
    total_caravan_space = caravan_space * 3

    # Calculate the remaining parking spaces
    remaining_spaces = total_spaces - total_caravan_space

    # Calculate the number of vehicles that can still park
    vehicles_park = remaining_spaces // total_spaces

    # return the result
    result = vehicles_park
    return result

print(solution())