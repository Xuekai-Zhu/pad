def solution():
    # Define the heights of the buildings
    tallest = 100
    second_tallest = tallest / 2
    third_tallest = second_tallest / 2
    fourth_tallest = third_tallest / 5

    # Calculate the total height of all buildings
    total_tall = tallest + second_tallest + third_tallest + fourth_tallest
    result = total_tall
    return result

print(solution())