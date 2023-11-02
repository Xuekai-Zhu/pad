def solution():
    machines_working_23_hours = 3
    machines_working_12_hours = 1
    hours_per_day = 24
    production_total_23_hours = machines_working_23_hours * hours_per_day
    production_total_12_hours = machines_working_12_hours * hours_per_day
    material_produced_per_hour = 2
    total_material_produced = production_total_23_hours + production_total_12_hours
    selling_price_per_kg = 50
    total_selling_price = selling_price_per_kg * total_material_produced
    result = total_selling_price
    
    return result

print(solution())