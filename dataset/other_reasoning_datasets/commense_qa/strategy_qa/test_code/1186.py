def solution():
    # Define the properties of Kaffir limes and the Sage and Citrus scent
    kaffir_lime_origin = "tropical climates"
    kaffir_lime_fragrance = "intense citrus"
    yankee_candle_scent = "Sage and Citrus"
    # Check if Kaffir lime would be a good candle ingredient based on its properties
    if kaffir_lime_origin == "tropical climates" and kaffir_lime_fragrance in yankee_candle_scent:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())