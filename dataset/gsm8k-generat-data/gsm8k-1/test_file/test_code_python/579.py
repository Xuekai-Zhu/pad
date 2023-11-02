def solution():
    """Judy bought a dozen cups and twice as many dishes as cups to take to the church's charity event. At the event, she found out that her friend had brought 40 cups and 20 more dishes than she had brought. What's the total number of utensils brought by the two?"""
    cups = 12
    dishes = cups * 2
    judy_cups = cups
    judy_dishes = dishes
    friend_cups = 40
    friend_dishes = judy_dishes + 20
    total_cups = judy_cups + friend_cups
    total_dishes = judy_dishes + friend_dishes
    total_utensils = total_cups + total_dishes
    result = total_utensils
    return result

print(solution())