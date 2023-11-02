def solution():
    # Let's assume James is currently x years old
    # Then 3 years ago, he was (x-3) years old
    # And 3 years ago, his age was 27: (x-3) = 27 => x = 30
    james_age = 30

    # In 5 years, James will be 35 and Matt will be twice his age
    # So 2 * James_age + 5 = Matt_age + 5
    # Therefore, Matt_age = 2 * James_age - 5
    matt_age = 2 * james_age - 5
    result = matt_age
    return result

print(solution())