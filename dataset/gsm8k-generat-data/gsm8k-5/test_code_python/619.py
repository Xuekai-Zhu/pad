def solution():
    dogs_walked = [7, 7, 7, 12, 9]  # Dogs walked on each day
    dollars_per_dog = 5  # Harry is paid $5 for each dog he walks

    # Calculate the total number of dogs walked in a week
    total_dogs_walked = sum(dogs_walked)

    # Calculate Harry's earnings for the week
    earnings = total_dogs_walked * dollars_per_dog

    result = earnings
    return result

print(solution())