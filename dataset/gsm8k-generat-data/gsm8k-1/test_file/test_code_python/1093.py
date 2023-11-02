def solution():
    """Mary and John got married last weekend. There were 20 private cars and 12 buses parked outside the church. After the ceremony, each bus carried 35 people and each car carried 3 people. How many people were inside the church?"""
    cars = 20
    buses = 12
    people_per_bus = 35
    people_per_car = 3
    total_people = (cars * people_per_car) + (buses * people_per_bus)
    result = total_people
    return result

print(solution())