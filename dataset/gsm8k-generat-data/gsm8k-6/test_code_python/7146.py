def solution():
    # Calculate the total volume of the spice paste
    total_volume = (3*3) + (1*1) + (1*1) + (2*3) + ((1*4)*3)  # convert teaspoons to tablespoons for consistency 

    # Calculate the volume of ginger in the spice paste
    ginger_volume = 3*3  # 3 tablespoons of ginger

    # Calculate the percentage of the spice paste that is ginger
    ginger_percentage = (ginger_volume / total_volume) * 100
    rounded_percentage = round(ginger_percentage)

    result = rounded_percentage
    return result

print(solution())