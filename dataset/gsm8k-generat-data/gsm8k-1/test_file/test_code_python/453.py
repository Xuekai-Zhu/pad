def solution():
    """While playing with her friends in their school playground, Katelyn saw 50 fairies flying above the nearby forest. After about twenty minutes, one of her friends saw half as many fairies as Katelyn saw come from the east and join the fairies that were there. Ten minutes later, 30 fairies flew away. How many fairies are remaining?"""
    katelyn_saw = 50
    friend_saw = katelyn_saw / 2
    total_fairies = katelyn_saw + friend_saw
    total_fairies -= 30
    result = total_fairies
    return result

print(solution())