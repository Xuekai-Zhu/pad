def solution():
    """Dora's father's age is eight more than twice Dora's age. If Dora's mother is four years younger than Dora's father, and Dora is 15 years old, calculate the total combined age of Dora, her father, and her mother."""
    dora_age = 15
    father_age = 8 + 2 * dora_age
    mother_age = father_age - 4
    total_age = dora_age + father_age + mother_age
    result = total_age
    return result

print(solution())