def solution():
    main_ingredients = ["rice", "black gram"]
    keto_diet = ["high-fat", "adequate-protein", "low-carbohydrate"]
    if "rice" in main_ingredients and "carbohydrate" in keto_diet:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())