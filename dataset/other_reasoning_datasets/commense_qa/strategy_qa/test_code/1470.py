def solution():
    causes_of_depression = ["low serotonin", "low dopamine", "low norepinephrine"]
    candy_bar_ingredients = ["Monoamine Oxidase"]
    if all(cause in candy_bar_ingredients for cause in causes_of_depression):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())