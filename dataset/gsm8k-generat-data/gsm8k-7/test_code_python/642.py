def solution():
    miles_to_groceries = 10
    miles_to_haircut = 15
    miles_to_doctor = 5

    # Calculate the total distance Tony will drive for all his errands
    total_distance = miles_to_groceries + miles_to_haircut + miles_to_doctor

    # Calculate the halfway point of Tony's total errands distance
    halfway_distance = total_distance / 2

    # Calculate how many miles Tony has driven so far
    miles_driven = 0
    if halfway_distance <= miles_to_groceries:
        miles_driven = halfway_distance
    elif halfway_distance <= (miles_to_groceries + miles_to_haircut):
        miles_driven = miles_to_groceries + (halfway_distance - miles_to_groceries) / 2
    else:
        miles_driven = total_distance - (halfway_distance - miles_to_groceries - miles_to_haircut) / 2
    result = miles_driven
    return result

print(solution())