def solution():
    """Ricky has 40 roses. His little sister steals 4 roses. If he wants to give away the rest of the roses in equal portions to 9 different people, how many roses will each person get?"""
    # Calculate the number of roses after the theft
    num_roses = 40 - 4

    # Calculate the number of roses each person will get
    roses_per_person = num_roses // 9

    # Display the number of roses each person will get
    result = roses_per_person
    return result

print(solution())