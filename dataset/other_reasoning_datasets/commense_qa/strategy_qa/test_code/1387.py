def solution():
    # Define the ingredients used in hamburger buns
    ingredients = ["sesame seeds", "beaten egg whites"]
    # Check if glue is used as an ingredient
    if "glue" not in ingredients:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())