def solution():
    # Define the type of melanoma that Bob Marley died from
    melanoma_type = "acral lentiginous melanoma"
    # Check if this type of melanoma is related to sun exposure
    if melanoma_type == "acral lentiginous melanoma":
        result = "Sunscreen would not have been helpful for this condition"
    else:
        result = "Sunscreen could have been helpful for preventing this condition"
    return result

print(solution())