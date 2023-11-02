def solution():
    """John gave his fiancee a $4000 ring on their engagement day, a $2000 car as a gift on their wedding day, and a diamond brace twice as expensive as the ring he gave her during the engagement. What's the worth of the presents John gave to her fiancee?"""
    # Define the value of the engagement ring and the wedding car
    ring_value = 4000
    car_value = 2000

    # Calculate the value of the diamond bracelet
    bracelet_value = ring_value * 2

    # Calculate the total worth of the presents
    total_worth = ring_value + car_value + bracelet_value

    # return the result
    result = total_worth
    return result

print(solution())