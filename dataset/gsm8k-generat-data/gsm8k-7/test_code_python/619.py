def solution():
    dogs_per_day = [7, 7, 12, 9]
    pay_per_dog = 5
    total_days = len(dogs_per_day)
    total_dogs = sum(dogs_per_day)

    # Calculate the total pay that Harry will earn for the week
    total_pay = total_dogs * pay_per_dog
    result = total_pay
    return result

print(solution())