def solution():
    """There are ten more newborn elephants than baby hippos. If an entire herd starts with 20 elephants and 35 hippos, and the female hippos, whose number is 5/7 of the total number of hippos, give birth to 5 new baby hippos each, find the number of animals that are there altogether?"""
    elephant_count = 20
    hippo_count = 35
    new_hippo_count = (5/7) * hippo_count * 5
    new_elephant_count = new_hippo_count + 10
    total_animals = elephant_count + hippo_count + new_hippo_count + new_elephant_count
    result = total_animals
    return result

print(solution())