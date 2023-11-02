def solution():
    """Tomas ate 1.5 pounds of chocolate fudge last week. Katya ate half a pound of peanut butter fudge, while Boris ate 2 pounds of fudge. How many ounces of fudge did the 3 friends eat in total?"""
    # Define the amounts of fudge eaten by each friend
    tomas_fudge = 1.5
    katya_fudge = 0.5
    boris_fudge = 2.0

    # Convert the amounts to ounces
    tomas_ounces = tomas_fudge * 16
    katya_ounces = katya_fudge * 16
    boris_ounces = boris_fudge * 16

    # Calculate the total amount of fudge eaten in ounces
    total_ounces = tomas_ounces + katya_ounces + boris_ounces

    # return the result
    result = total_ounces
    return result

print(solution())