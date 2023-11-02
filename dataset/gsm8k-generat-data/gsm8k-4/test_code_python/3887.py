def solution():
    """Bingo has two dogs. On average, they walk a total of 70 miles a week. The first dog walks an average of 2 miles a day. How many miles a day does the other dog average?"""
    # Define the total distance walked by both dogs
    total_distance = 70

    # Define the distance walked by the first dog
    first_dog_distance = 2 * 7 # 2 miles a day for 7 days a week

    # Calculate the distance walked by the second dog
    second_dog_distance = total_distance - first_dog_distance

    # Calculate the average distance walked by the second dog
    second_dog_average = second_dog_distance / 7

    # Return the result
    result = second_dog_average
    return result

print(solution())