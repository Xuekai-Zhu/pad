def solution():
    bundles = 3
    bunches = 2
    heaps = 5
    sheets_per_bundle = 2
    sheets_per_bunch = 4
    sheets_per_heap = 20
    total_sheets = bundles * sheets_per_bundle + bunches * sheets_per_bunch + heaps * sheets_per_heap
    result = total_sheets
    return result

print(solution())