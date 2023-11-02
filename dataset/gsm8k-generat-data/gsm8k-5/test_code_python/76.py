def solution():
    potatoes = 237  # There are 237 potatoes
    cucumbers = potatoes - 60  # There are 60 fewer cucumbers than potatoes
    peppers = 2 * cucumbers  # There are twice as many peppers as cucumbers
    total_vegetables = potatoes + cucumbers + peppers  # Calculate the total number of vegetables

    result = total_vegetables
    return result

print(solution())