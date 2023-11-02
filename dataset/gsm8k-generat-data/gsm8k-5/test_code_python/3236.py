def solution():
    # Ricky had 40 roses, but his sister stole 4, so he has 36 roses left
    total_roses = 36

    # Ricky wants to give away the roses in equal portions to 9 people
    num_people = 9

    # Divide the total number of roses by the number of people to get the number of roses each person will receive
    roses_per_person = total_roses / num_people
    result = roses_per_person
    return result

print(solution())