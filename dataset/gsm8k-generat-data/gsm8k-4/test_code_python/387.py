def solution():
    """Nellie can eat 12 sourball candies before crying. Jacob can only manage half of that number of candies,
    and Lana can only do three fewer than Jacob. They had a bucket of 30 candies, and all of them ate until they cried.
    If they divide the remaining candies in the bucket equally, how many sourball candies will they each get?"""
    
    # Define the number of candies Nellie can eat before crying
    nellie_candies = 12

    # Define the number of candies Jacob can eat before crying
    jacob_candies = nellie_candies / 2

    # Define the number of candies Lana can eat before crying
    lana_candies = jacob_candies - 3

    # Calculate the total number of candies they ate before crying
    total_candies_consumed = nellie_candies + jacob_candies + lana_candies

    # Calculate the total number of candies remaining in the bucket
    total_candies_remaining = 30 - total_candies_consumed

    # Calculate the number of candies each of them will get if they divide the remaining candies equally
    candies_per_person = total_candies_remaining / 3

    # return the result
    result = candies_per_person
    return result

print(solution())