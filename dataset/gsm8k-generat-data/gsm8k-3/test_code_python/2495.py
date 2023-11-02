def solution():
    """A thirsty traveler found an oasis in the desert. He drank 32 ounces of water. His camel drank seven times as much as he did. There are 128 ounces in a gallon. How many gallons of water did they drink altogether?"""
    # Define the amount of water the traveler and camel drank in total
    total_drink = 32 + 7 * 32

    # Convert the total amount of water to gallons
    gallons = total_drink / 128

    # Display the answer in gallons
    result = gallons
    return result

print(solution())