def solution():
    """Jenny is older than Charlie by five years, while Charlie is older than Bobby by three years. How old will Charlie be when Jenny becomes twice as old as Bobby?"""
    # Let's assume Bobby's age is 'x'
    bobby_age = x
    # Charlie is 3 years older than Bobby
    charlie_age = bobby_age + 3
    # Jenny is 5 years older than Charlie (and 8 years older than Bobby)
    jenny_age = charlie_age + 5

    # We want to find the age of Charlie when Jenny becomes twice as old as Bobby
    # Let's assume Y is the number of years from now when this happens.
    # After Y years, Jenny will be jenny_age + Y years old,
    # Bobby will be x + Y years old, and Charlie will be charlie_age + Y years old
    # We want Jenny's age to be twice Bobby's age at that point:
    # jenny_age + Y = 2*(x + Y)
    # Rearranging the terms, we get:
    # Y = (jenny_age - 2*x) / (2 - 1)

    y = (jenny_age - 2 * bobby_age) / (2 - 1)
    # The age of Charlie in Y years will be charlie_age + Y
    charlie_age_in_Y_years = charlie_age + y
    return charlie_age_in_Y_years

print(solution())