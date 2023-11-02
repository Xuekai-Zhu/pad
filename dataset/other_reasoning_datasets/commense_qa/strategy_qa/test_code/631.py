def solution():
    # Define the professions
    professions = ["dentist", "IT professional"]
    # Define the problematic entities
    problematic_entities = ["technological problems", "Bluetooth"]
    # Check if a dentist treats any of the problematic entities
    if "dentist" in professions and any(entity in ["diseases and conditions of the oral cavity"] for entity in problematic_entities):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())