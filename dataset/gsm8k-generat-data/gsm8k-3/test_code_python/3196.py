def solution():
    """Mark has 30 candies, Peter has 25 candies, and John has 35 candies. They decided to combine their candies together and share them equally. How many candies will each one of them have?"""
    # Calculate the total number of candies
    total_candies = 30 + 25 + 35

    # Calculate how many candies each person will have
    candies_per_person = total_candies // 3

    # Display how many candies each person will have
    result = candies_per_person
    return result

print(solution())