def solution():
    # Find the height of each building
    tallest = 100
    second_tallest = tallest / 2
    third_tallest = second_tallest / 2
    fourth_tallest = third_tallest / 5

    # Calculate the total height of all 4 buildings
    total_height = tallest + second_tallest + third_tallest + fourth_tallest
    result = total_height
    return result

print(solution())