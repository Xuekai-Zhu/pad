def solution():
    """Timmy, Tommy and Tina are filling up a kiddie pool in their backyard. Each has a pail they fill with water from a house before dumping it into the pool. If Timmy's pail holds twice as much water as Tommy's, and Tommy's holds 2 gallons more than Tina's, and Tina's is 4 gallons, how much water do the three of them fill the pool with after 3 trips each?"""
    tina_pail = 4
    tommy_pail = tina_pail + 2
    timmy_pail = tommy_pail * 2
    total_water = 0
    for i in range(3):
        total_water += (tina_pail + tommy_pail + timmy_pail)
    result = total_water
    return result

print(solution())