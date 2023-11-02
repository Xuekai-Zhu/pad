def solution():
    minutes_per_dog = 20  # Jennifer takes 20 minutes to groom each of her 2 dogs
    dogs = 2  # Jennifer has 2 dogs
    days = 30  # Jennifer wants to know how many hours she will spend grooming her dogs in 30 days

    # Calculate the total minutes Jennifer spends grooming her dogs in 30 days
    total_minutes = minutes_per_dog * dogs * days

    # Convert the total minutes to hours
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())