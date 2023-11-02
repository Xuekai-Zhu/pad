def solution():
    
    monday_wednesday_friday_dogs = 7
    tuesday_dogs = 12
    thursday_dogs = 9
    price_per_dog_walk = 5
    total_dog_walks = (monday_wednesday_friday_dogs * 3) + tuesday_dogs + thursday_dogs
    total_earnings = total_dog_walks * price_per_dog_walk
    result = total_earnings
    return result

print(solution())