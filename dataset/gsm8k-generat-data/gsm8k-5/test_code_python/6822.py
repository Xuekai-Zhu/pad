def solution():
    pages_per_minute_meso = 15 / 5  # Meso can type 15 pages in 5 minutes
    pages_per_minute_tyler = 15 / 3  # Tyler can type 15 pages in 3 minutes
    pages_to_type = 40  # Meso and Tyler need to type 40 pages together

    # Calculate the time it would take Meso and Tyler to type 40 pages working together
    time_to_type_40_pages = pages_to_type / (pages_per_minute_meso + pages_per_minute_tyler)
    result = time_to_type_40_pages
    return result

print(solution())