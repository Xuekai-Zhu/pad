def solution():
    """Howie wants to buy cupcakes for everyone in his class as a special treat. He's not sure if people will want vanilla or chocolate cupcakes so he decides to get one of each for everyone. If he gets the same amount of 2 cupcakes for each himself, his teacher, and his 25 classmates, how many cupcakes should Howie buy?"""
    num_people = 27 # Howie + his teacher + 25 classmates
    num_cupcakes_per_person = 2 # 1 vanilla + 1 chocolate
    total_cupcakes = num_people * num_cupcakes_per_person
    result = total_cupcakes
    return result

print(solution())