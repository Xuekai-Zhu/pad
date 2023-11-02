def solution():
    tallest_building = 100
    second_tallest_building = tallest_building / 2
    third_tallest_building = second_tallest_building / 2
    fourth_tallest_building = third_tallest_building / 5

    # Calculate the total height of all four buildings
    total_height = tallest_building + second_tallest_building + third_tallest_building + fourth_tallest_building
    result = total_height
    return result

print(solution())