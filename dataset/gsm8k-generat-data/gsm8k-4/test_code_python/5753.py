def solution():
    """There are 55 people at the track meet. 30 of them are boys, and the rest are girls. Three fifths of the girls have long hair, and the rest have short hair. How many girls have short hair?"""
    # Define the total number of people and the number of boys
    total_people = 55
    boys = 30

    # Calculate the number of girls
    girls = total_people - boys

    # Calculate the number of girls with long hair
    long_hair_girls = (3/5) * girls

    # Calculate the number of girls with short hair
    short_hair_girls = girls - long_hair_girls

    # Return the result
    result = short_hair_girls
    return result

print(solution())