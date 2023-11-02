def solution():
    """At camp Wonka, there are 96 campers. Two-thirds of the campers are boys, and the remaining one-third are girls. 50% of the boys want to toast marshmallows and 75% of the girls want to toast marshmallows. If each camper gets one marshmallow to toast, how many marshmallows do they need?"""
    # Define the total number of campers and calculate the number of boys and girls
    total_campers = 96
    boys = total_campers * (2/3)
    girls = total_campers * (1/3)

    # Calculate the number of boys and girls who want to toast marshmallows
    boys_toast = boys * 0.5
    girls_toast = girls * 0.75

    # Calculate the total number of marshmallows needed
    total_marshmallows = boys_toast + girls_toast

    # Return the result
    result = total_marshmallows
    return result

print(solution())