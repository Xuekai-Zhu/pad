def solution():
    """Mark has 30 candies, Peter has 25 candies, and John has 35 candies. They decided to combine their candies together and share them equally. How many candies will each one of them have?"""
    total_candies = 30 + 25 + 35
    num_people = 3
    candies_per_person = total_candies / num_people
    result = candies_per_person
    return result

print(solution())