def solution():
    population = 80
    people_driving = population
    people_taking_bus = population * .25
    total_people = population - people_taking_bus
    carbon_emitted_by_cars = people_driving * 10
    carbon_emitted_by_buses = people_taking_bus * 100
    total_carbon_emitted = carbon_emitted_by_cars + carbon_emitted_by_buses
    resulting_carbon_emitted = total_carbon_emitted - carbon_emitted_by_buses
    return resulting_carbon_emitted

print(solution())