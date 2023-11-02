def solution():
    """Bingo has two dogs. On average, they walk a total of 70 miles a week. The first dog walks an average of 2 miles a day. How many miles a day does the other dog average?"""
    # Define variables
    total_miles = 70
    first_dog_miles = 2 * 7  # 2 miles a day for 7 days

    # Calculate the average miles per day for the second dog
    second_dog_miles = (total_miles - first_dog_miles) / 7

    # Return the result
    result = second_dog_miles
    return result

print(solution())