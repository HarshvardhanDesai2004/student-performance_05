"""CGPA calculation (AI-generated draft v1 - contains a defect, see journal #4)."""

GRADE_POINTS = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "P": 4, "F": 0}


def calculate_cgpa(courses):
    total = 0
    for grade, credits in courses:
        total += GRADE_POINTS[grade] * credits
    return round(total / len(courses), 2)
