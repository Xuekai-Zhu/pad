def solution():
    tallest = 100  # Height of the tallest building in feet
    second_tallest = tallest / 2  # Height of the second tallest building in feet
    third_tallest = second_tallest / 2  # Height of the third tallest building in feet
    fourth_tallest = third_tallest / 5  # Height of the fourth tallest building in feet

    # Calculate the total height of all four buildings
    total_height = tallest + second_tallest + third_tallest + fourth_tallest
    result = total_height
    return result

print(solution())