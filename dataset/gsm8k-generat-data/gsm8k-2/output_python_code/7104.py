def solution():
    """The city of Richmond has 1000 more people than Victoria. Victoria has 4 times as many people as Beacon. If Richmond has 3000 people, how many people are there in Beacon?"""
    richmond = 3000
    victoria = richmond - 1000
    beacon = victoria / 4
    result = beacon
    return result

print(solution())