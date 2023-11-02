def solution():
    total_flowers = 52
    flowers_given_to_mom = 15
    flowers_given_to_grandma = flowers_given_to_mom + 6

    # Calculate the total number of flowers that Lara kept for herself
    flowers_kept = total_flowers - (flowers_given_to_mom + flowers_given_to_grandma)

    result = flowers_kept
    return result

print(solution())