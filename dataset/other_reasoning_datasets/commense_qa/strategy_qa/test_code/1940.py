def solution():
    constitution_words = 7500
    hobbit_words = 95356
    # Assuming the proofreader gets paid the same rate per word for both documents
    if hobbit_words > constitution_words:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())