def solution():
    # Define the ages of Kaydence's family members
    father_age = 60
    mother_age = father_age - 2
    brother_age = 0.5 * father_age
    sister_age = 40

    # Calculate the total age of Kaydence's family members (excluding Kaydence)
    total_age = father_age + mother_age + brother_age + sister_age

    # Calculate Kaydence's age
    kaydence_age = 200 - total_age
    result = kaydence_age
    return result

print(solution())