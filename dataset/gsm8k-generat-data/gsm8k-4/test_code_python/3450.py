def solution():
    """Carson needs to mow the lawn and plant some flowers. Carson has to mow 40 lines to cover the whole yard, and it takes him 2 minutes to mow one line. He also needs to plant 8 rows of flowers, each with 7 flowers, and it takes him half a minute to plant each flower. How many minutes will Carson spend gardening?"""
    # Calculate the time it takes Carson to mow the lawn
    lawn_mowing_time = 40 * 2

    # Calculate the number of flowers Carson needs to plant
    num_flowers = 8 * 7

    # Calculate the time it takes Carson to plant one flower
    flower_planting_time = 0.5

    # Calculate the total time it takes Carson to plant all the flowers
    flower_planting_total_time = num_flowers * flower_planting_time

    # Calculate the total time Carson spends gardening
    total_gardening_time = lawn_mowing_time + flower_planting_total_time

    # Return the result
    result = total_gardening_time
    return result

print(solution())