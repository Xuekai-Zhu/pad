def solution():
    """Harry is a professional dog-walker. He is paid to go on long walks with dogs while their families are away from home. On Monday, Wednesday, and Friday, Harry walks 7 dogs. On Tuesday, he walks 12 dogs. And on Thursday he walks 9 dogs. He is paid $5 for each dog that he walks. How many dollars does Harry earn in a week?"""
    monday_wednesday_friday_dogs = 7
    tuesday_dogs = 12
    thursday_dogs = 9
    price_per_dog_walk = 5
    total_dog_walks = (monday_wednesday_friday_dogs * 3) + tuesday_dogs + thursday_dogs
    total_earnings = total_dog_walks * price_per_dog_walk
    result = total_earnings
    return result

print(solution())