def solution():
    # Define the properties of a firewall and a hammer
    is_firewall_physical = False
    can_hammers_destroy_non_physical_entities = False
    # Check if a firewall can be destroyed by a hammer
    if is_firewall_physical and can_hammers_destroy_non_physical_entities:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())