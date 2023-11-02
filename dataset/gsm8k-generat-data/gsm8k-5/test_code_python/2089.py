def solution():
    pie_left = 1200  # The weight of the pie left in the fridge is 1200 grams
    fraction_eaten = 1/6  # Sophia ate 1/6 of the pie

    # Calculate the weight of the pie Sophia ate
    weight_eaten = pie_left / fraction_eaten - pie_left
    result = weight_eaten
    return result

print(solution())