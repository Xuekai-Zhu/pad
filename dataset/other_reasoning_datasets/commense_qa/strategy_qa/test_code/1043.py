def solution():
    medication_type = "SSRI"
    citrus_fruit = "grapefruit"
    affected_medications = ["SSRI"]
    if citrus_fruit == "grapefruit" and medication_type in affected_medications:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())