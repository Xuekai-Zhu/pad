def solution():
    model_thinness = "very thin"
    cookout_food = "high calorie American style barbecue"
    pressure_to_maintain_weight = True
    if model_thinness == "very thin" and pressure_to_maintain_weight and cookout_food != "low calorie options":
        result = "no"
    else:
        result = "yes"
    return result

print(solution())