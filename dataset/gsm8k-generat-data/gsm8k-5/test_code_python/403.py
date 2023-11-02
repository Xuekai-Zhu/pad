def solution():
    kimiko_age = 28  # given
    omi_age = 2 * kimiko_age  # Omi is twice as old as Kimiko
    arlette_age = (3/4) * kimiko_age  # Arlette is 3/4 times as old as Kimiko

    # Calculate the average age of the three
    average_age = (kimiko_age + omi_age + arlette_age) / 3
    result = average_age
    return result

print(solution())