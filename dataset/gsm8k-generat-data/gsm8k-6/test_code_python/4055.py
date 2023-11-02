def solution():
    # Calculate the total number of people on the carousel
    total_people = 4 + 30  # four clowns and thirty children
    # Calculate the total number of candies sold
    total_candies_sold = 20 * total_people
    # Calculate the number of candies left with the candy seller
    candies_left = 700 - total_candies_sold
    result = candies_left
    return result

print(solution())