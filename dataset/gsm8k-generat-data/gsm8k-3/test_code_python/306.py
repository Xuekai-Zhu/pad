def solution():
    """Cary is an engineer in charge of designing an irrigation system for three farmers. Farmer Bob grows 3 acres of corn, 9 acres of cotton, and 12 acres of beans. Farmer Brenda grows 6 acres of corn, 7 acres of cotton, and 14 acres of beans. Farmer Bernie grows 2 acres of corn and 12 acres of cotton. If corn takes 20 gallons of water an acre, cotton takes 80 gallons of water an acre, and beans take twice as much water as corn, what percentage of the total water used will go to Farmer Bob's farm?"""
    # Define the number of acres for each farmer
    bob_corn_acres = 3
    bob_cotton_acres = 9
    bob_bean_acres = 12

    brenda_corn_acres = 6
    brenda_cotton_acres = 7
    brenda_bean_acres = 14

    bernie_corn_acres = 2
    bernie_cotton_acres = 12

    # Define the water usage for each crop
    corn_water_usage = 20
    cotton_water_usage = 80
    bean_water_usage = corn_water_usage * 2

    # Calculate the total water usage for each farmer
    bob_water_usage = (bob_corn_acres * corn_water_usage) + (bob_cotton_acres * cotton_water_usage) + (bob_bean_acres * bean_water_usage)
    brenda_water_usage = (brenda_corn_acres * corn_water_usage) + (brenda_cotton_acres * cotton_water_usage) + (brenda_bean_acres * bean_water_usage)
    bernie_water_usage = (bernie_corn_acres * corn_water_usage) + (bernie_cotton_acres * cotton_water_usage)

    # Calculate the total water usage
    total_water_usage = bob_water_usage + brenda_water_usage + bernie_water_usage

    # Calculate the percentage of water used by Bob
    bob_percent = (bob_water_usage / total_water_usage) * 100

    # Display the percentage of water used by Bob
    result = bob_percent
    return result

print(solution())