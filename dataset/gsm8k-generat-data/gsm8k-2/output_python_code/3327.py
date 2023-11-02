def solution():
    """Arthur has 3 dogs. They eat an average of 15 pounds of food a week. One dog eats 13 pounds a week. The second eats double this. How much does the third dog eat a week?"""
    total_dog_food = 15 * 3
    second_dog_food = 13 * 2
    third_dog_food = total_dog_food - (13 + second_dog_food)
    result = third_dog_food
    return result

print(solution())