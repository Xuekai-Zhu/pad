def solution():
    cat_name = "Sockington"
    onion_toxicity = False
    if onion_toxicity:
        result = f"{cat_name} does not enjoy onions because they are toxic for cats."
    else:
        result = f"{cat_name} probably does not enjoy onions, but it is not because of their toxicity to cats."
    return result

print(solution())