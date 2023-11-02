def solution():
    number_of_people = 4 + 30  # Four clowns and thirty children go on a carousel
    candies_sold = number_of_people * 20  # Each person bought 20 candies
    candies_left = 700 - candies_sold  # The candy seller had 700 candies to start with
    result = candies_left
    return result

print(solution())