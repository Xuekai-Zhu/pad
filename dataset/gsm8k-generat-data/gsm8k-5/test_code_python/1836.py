def solution():
    # Total number of candies each person has
    billy_candies = 6 + 8  # Billy started with 6 candies and got 8 more from his father
    caleb_candies = 11 + 11  # Caleb started with 11 candies and got 11 more from his father
    andy_candies = 9 + (36 - 8 - 11)  # Andy started with 9 candies and got the rest from his father

    # Difference between the number of candies Andy and Caleb have
    difference = andy_candies - caleb_candies
    result = difference
    return result

print(solution())