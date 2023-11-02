def solution():
    """Cary is an engineer in charge of designing an irrigation system for three farmers. Farmer Bob grows 3 acres of corn, 9 acres of cotton, and 12 acres of beans. Farmer Brenda grows 6 acres of corn, 7 acres of cotton, and 14 acres of beans. Farmer Bernie grows 2 acres of corn and 12 acres of cotton. If corn takes 20 gallons of water an acre, cotton takes 80 gallons of water an acre, and beans take twice as much water as corn, what percentage of the total water used will go to Farmer Bob's farm?"""
    bob_corn_acres = 3
    bob_cotton_acres = 9
    bob_bean_acres = 12
    brenda_corn_acres = 6
    brenda_cotton_acres = 7
    brenda_bean_acres = 14
    bernie_corn_acres = 2
    bernie_cotton_acres = 12

    total_water = bob_corn_acres * 20 + bob_cotton_acres * 80 * \
                  2 + bob_bean_acres * 20 * 2 + brenda_corn_acres * \
                  20 + brenda_cotton_acres * 80 * 2 + brenda_bean_acres * \
                  20 * 2 + bernie_corn_acres * 20 + bernie_cotton_acres * 80

    bob_water = bob_corn_acres * 20 + bob_cotton_acres * 80 * 2 + bob_bean_acres * 20 * 2
    bob_percent = (bob_water / total_water) * 100

    result = bob_percent
    return result

print(solution())