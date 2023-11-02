def solution():
    num_blouses = 100
    dots_per_blouse = 20
    ml_per_dot = 10
    ml_per_bottle = 400

    # Calculate the total number of dots needed for all blouses
    total_dots = num_blouses * dots_per_blouse

    # Calculate the total ml of dye needed for all dots
    total_ml = total_dots * ml_per_dot

    # Calculate the total number of bottles needed
    total_bottles = total_ml / ml_per_bottle
    result = total_bottles
    return result

print(solution())