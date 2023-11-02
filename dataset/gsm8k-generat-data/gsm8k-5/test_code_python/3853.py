def solution():
    calories_per_cheesecake = 2800  # A cheesecake contains 2800 calories
    calories_per_slice = 350  # Each slice of cheesecake contains 350 calories
    kiley_percent = 25  # Kiley ate 25% of the cheesecake

    # Calculate the total calories Kiley ate
    calories_eaten = calories_per_cheesecake * (kiley_percent / 100)

    # Calculate the number of slices Kiley ate
    slices_eaten = calories_eaten / calories_per_slice
    result = slices_eaten
    return result

print(solution())