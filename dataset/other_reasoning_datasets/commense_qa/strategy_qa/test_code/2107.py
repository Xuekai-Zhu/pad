def solution():
    # Define the properties of hair and furniture cushions
    hair_durability = "durable"
    cushion_material = "horse hair"
    # Check if furniture can be made of hair
    if hair_durability == "durable" and cushion_material == "horse hair":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())