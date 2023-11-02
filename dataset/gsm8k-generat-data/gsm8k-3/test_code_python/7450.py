def solution():
    """At camp Wonka, there are 96 campers.  Two-thirds of the campers are boys, and the remaining one-third are girls.  50% of the boys want to toast marshmallows and 75% of the girls want to toast marshmallows.  If each camper gets one marshmallow to toast, how many marshmallows do they need?"""
    # Define the number of campers and the ratios of boys and girls
    num_campers = 96
    boy_ratio = 2/3
    girl_ratio = 1 - boy_ratio

    # Calculate the number of boys and girls
    num_boys = int(num_campers * boy_ratio)
    num_girls = num_campers - num_boys

    # Calculate the number of boys and girls who want to toast marshmallows
    num_boy_marshmallow = int(num_boys * 0.5)
    num_girl_marshmallow = int(num_girls * 0.75)

    # Calculate the total number of marshmallows needed
    total_marshmallow = num_boy_marshmallow + num_girl_marshmallow

    # Display the total number of marshmallows needed
    result = total_marshmallow
    return result

print(solution())