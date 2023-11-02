def solution():
    """If Mark weighs 150 pounds and Susan weighs 20 pounds less than Mark. And their friend Bob weighs twice as much as Susan. What is the average weight of the 3 friends?"""
    mark_weight = 150
    susan_weight = mark_weight - 20
    bob_weight = susan_weight * 2
    total_weight = mark_weight + susan_weight + bob_weight
    average_weight = total_weight / 3
    result = average_weight
    return result

print(solution())