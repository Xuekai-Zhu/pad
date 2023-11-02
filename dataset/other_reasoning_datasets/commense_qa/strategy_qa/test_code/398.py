def solution():
    # Define the native regions of the European wildcat and the black-tailed jackrabbit
    european_wildcat_native_regions = ["Europe", "Scotland", "Turkey", "Caucasus"]
    black_tailed_jackrabbit_native_regions = ["Mexico", "Western United States"]
    # Check if the black-tailed jackrabbit is afraid of the European wildcat
    if "Europe" in black_tailed_jackrabbit_native_regions or "Scotland" in black_tailed_jackrabbit_native_regions or "Turkey" in black_tailed_jackrabbit_native_regions or "Caucasus" in black_tailed_jackrabbit_native_regions:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())