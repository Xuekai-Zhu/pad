def solution():
    """Daisy bought a bag of potatoes that weighed 5 pounds. She also bought a bag of sweet potatoes that weighed 2 times as much as the potatoes and a bag of carrots that weighed 3 pounds fewer than the sweet potatoes. How many pounds of carrots did Daisy buy?"""
    potato_weight = 5
    sweet_potato_weight = potato_weight * 2
    carrot_weight = sweet_potato_weight - 3
    result = carrot_weight
    return result

print(solution())