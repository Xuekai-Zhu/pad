def solution():
    # Calculate the number of hours of boring gameplay
    boring_gameplay = 0.8 * 100

    # Calculate the total hours of gameplay including the expansion
    total_gameplay = boring_gameplay + 30 + 100

    # Calculate the number of hours of enjoyable gameplay
    enjoyable_gameplay = total_gameplay - boring_gameplay

    result = enjoyable_gameplay
    return result

print(solution())