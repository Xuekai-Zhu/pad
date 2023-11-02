def solution():
    tanya_age = 60  # Tanya is 60 years old
    john_age = tanya_age / 2  # John is half as old as Tanya
    mary_age = john_age / 2  # John is twice as old as Mary
    
    # Calculate the total age of the three of them
    total_age = john_age + mary_age + tanya_age

    # Calculate the average age
    avg_age = total_age / 3
    result = avg_age
    return result

print(solution())