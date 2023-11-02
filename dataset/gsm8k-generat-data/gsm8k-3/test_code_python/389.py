def solution():
    """Nellie can eat 12 sourball candies before crying. Jacob can only manage half of that number of candies, and Lana can only do three fewer than Jacob. They had a bucket of 30 candies, and all of them ate until they cried. If they divide the remaining candies in the bucket equally, how many sourball candies will they each get?"""
    # Determine how many sourballs each person can eat before crying
    nellie_limit = 12
    jacob_limit = nellie_limit // 2
    lana_limit = jacob_limit - 3

    # Determine how many sourballs all three can eat before crying
    total_limit = nellie_limit + jacob_limit + lana_limit

    # Determine how many sourballs are left in the bucket
    remaining_candies = 30 - total_limit

    # Divide the remaining candies equally among the three people
    candies_per_person = remaining_candies // 3

    result = candies_per_person
    return result

print(solution())