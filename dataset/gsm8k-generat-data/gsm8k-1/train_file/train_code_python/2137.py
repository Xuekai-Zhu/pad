def solution():
    """A carpenter made ten tables for this month. Last month, he made three fewer tables than this month. How many tables did the carpenter make in total?"""
    tables_this_month = 10
    tables_last_month = tables_this_month - 3
    total_tables = tables_this_month + tables_last_month
    result = total_tables
    return result

print(solution())