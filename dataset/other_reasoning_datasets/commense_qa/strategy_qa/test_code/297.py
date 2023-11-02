def solution():
    # Define the properties of petroleum and petroleum jelly
    petroleum_reactivity = "high"
    petroleum_jelly_reactivity = "low"
    # Determine if petroleum jelly can be used as fuel
    if petroleum_jelly_reactivity == "low":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())