def solution():
    # Find the amount of money Elsa and Elizabeth spent
    elsa_spent = 2 * 58  # Elsa spent twice as much as Emma
    elizabeth_spent = 4 * elsa_spent  # Elizabeth spent four times as much as Elsa

    # Calculate the total amount of money spent by all three
    total_spent = emma_spent + elsa_spent + elizabeth_spent
    result = total_spent
    return result

print(solution())