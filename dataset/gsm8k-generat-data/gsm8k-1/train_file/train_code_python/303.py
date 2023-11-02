def solution():
    """Cary is an engineer in charge of designing an irrigation system for three farmers. Farmer Bob grows 3 acres of corn, 9 acres of cotton, and 12 acres of beans. Farmer Brenda grows 6 acres of corn, 7 acres of cotton, and 14 acres of beans. Farmer Bernie grows 2 acres of corn and 12 acres of cotton. If corn takes 20 gallons of water an acre, cotton takes 80 gallons of water an acre, and beans take twice as much water as corn, what percentage of the total water used will go to Farmer Bob's farm?"""
    corn_water = 20
    cotton_water = 80
    beans_water = corn_water * 2
    bob_water = (3 * corn_water) + (9 * cotton_water) + (12 * beans_water)
    brenda_water = (6 * corn_water) + (7 * cotton_water) + (14 * beans_water)
    bernie_water = (2 * corn_water) + (12 * cotton_water)
    total_water = bob_water + brenda_water + bernie_water
    bob_percent = (bob_water / total_water) * 100
    result = bob_percent
    return result

print(solution())