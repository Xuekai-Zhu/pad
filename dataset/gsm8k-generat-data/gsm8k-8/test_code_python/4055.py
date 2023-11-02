def solution():
    # Calculate the total number of people on the carousel
    total_people = 4 + 30

    # Calculate the total number of candies sold
    total_candies_sold = total_people * 20

    # Calculate the number of candies the seller has left
    candies_left = 700 - total_candies_sold
    result = candies_left
    return result

print(solution())