def solution():
    # Define the initial amount of popcorn
    buttered_popcorn = 12
    caramel_popcorn = 10

    # Subtract the popcorn that Alan took
    buttered_popcorn -= 3
    caramel_popcorn -= 1

    # Calculate the total amount of popcorn left
    total_popcorn = buttered_popcorn + caramel_popcorn

    result = total_popcorn
    return result

print(solution())