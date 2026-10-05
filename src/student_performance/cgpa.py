"""CGPA calculation (v2 - debugged: credit-weighted, validated)."""

GRADE_POINTS = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "P": 4, "F": 0}


def calculate_cgpa(courses):
    if not courses:
        raise ValueError("courses must not be empty")
    total_points = 0
    total_credits = 0
    for grade, credits in courses:
        if grade not in GRADE_POINTS:
            raise ValueError(f"unknown grade: {grade!r}")
        if credits <= 0:
            raise ValueError("credits must be positive")
        total_points += GRADE_POINTS[grade] * credits
        total_credits += credits
    return round(total_points / total_credits, 2)
