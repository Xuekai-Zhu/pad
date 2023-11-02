def solution():
    
    # Define John's current age
    john_age = 28

    # Calculate Jim's age when it came out John
    jim_age_when_john_was_out = john_age - 2

    # Calculate Jim's current age
    jim_age = john_age_when_john_was_out / 2

    # Display Jim's current age
    result = jim_age
    return result

print(solution())