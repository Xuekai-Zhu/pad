def solution():
    # Define the relationship between chlorine and household bleach
    chlorine_creates_bleach = True
    bleach_available_at_dollar_stores = True
    # Check if chlorine is available at dollar stores
    if chlorine_creates_bleach and bleach_available_at_dollar_stores:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())