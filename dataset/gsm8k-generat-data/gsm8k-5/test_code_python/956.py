def solution():
    garden_size = 64  # Joel's garden is 64 square feet large
    fruit_section_size = garden_size / 2  # Joel wants to use half of the garden for fruits
    vegetable_section_size = garden_size / 2  # Joel wants to use half of the garden for vegetables
    strawberry_section_size = fruit_section_size / 4  # Joel wants to use a quarter of the fruit section for strawberries

    result = strawberry_section_size
    return result

print(solution())