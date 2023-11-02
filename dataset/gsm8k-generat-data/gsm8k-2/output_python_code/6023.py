def solution():
    """Ellis is going to take a road trip with her family. First, she needs to figure out how many bottles of water she should bring for everyone. There will be four people total: Ellis, her mother, her sister, and her aunt. They will be on the road to their destination for 8 hours and drive 8 hours to return home. Every hour each person will want to drink 1/2 a bottle of water. How many water bottles will Ellis' family need total?"""
    num_people = 4
    travel_time = 16 # 8 hours to destination and 8 hours to return home
    water_per_person_per_hour = 0.5
    total_water = num_people * travel_time * water_per_person_per_hour
    result = total_water
    return result

print(solution())