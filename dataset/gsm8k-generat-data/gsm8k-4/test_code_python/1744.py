def solution():
    """A farmer harvested 250 potatoes. He bundled them in twenty-five's and sold each bundle for $1.90. He also harvested 320 carrots and bundled them in twenty's and sold each bundle for $2. If the farmer sold all his harvested crops, how much did he get in all?"""
    # Define the number of potatoes and carrots harvested
    num_potatoes = 250
    num_carrots = 320

    # Calculate the total number of potato bundles and carrot bundles
    num_potato_bundles = num_potatoes // 25
    num_carrot_bundles = num_carrots // 20

    # Calculate the total earnings from potato bundles and carrot bundles
    potato_earnings = num_potato_bundles * 1.9
    carrot_earnings = num_carrot_bundles * 2

    # Calculate the total earnings from selling all the harvested crops
    total_earnings = potato_earnings + carrot_earnings

    # return the result
    result = total_earnings
    return result

print(solution())