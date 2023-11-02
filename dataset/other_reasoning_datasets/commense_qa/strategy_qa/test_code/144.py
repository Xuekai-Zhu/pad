def solution():
    dominican_order_vows = ["poverty", "chastity", "obedience"]
    knights_hospitaller_training = "well trained"
    knights_hospitaller_military = "yes"
    if knights_hospitaller_training == "well trained" and knights_hospitaller_military == "yes":
        result = "It is uncertain, as training and military expertise are important factors in combat."
    else:
        result = "It is uncertain, as more information is needed about the capabilities of both orders."
    return result

print(solution())