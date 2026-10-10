"""CGPA calculation and performance classification.

CGPA = sum(grade_point * credits) / sum(credits). The grade scale is read from
``config/grade_scale.json`` so it is not hard-coded.
"""

from __future__ import annotations

import json
import math
from collections.abc import Iterable
from functools import lru_cache
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "grade_scale.json"


@lru_cache(maxsize=1)
def load_grade_scale(path: Path = CONFIG_PATH) -> dict[str, int]:
    """Load the grade -> grade-point mapping from JSON config."""
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def _validate(grade: str, credits: float, scale: dict[str, int]) -> None:
    if not isinstance(grade, str):
        raise ValueError("grade must be a string")
    if grade not in scale:
        raise ValueError(f"unknown grade: {grade!r}")
    if isinstance(credits, bool) or not isinstance(credits, int | float):
        raise ValueError("credits must be a positive number")
    numeric_credits = float(credits)
    if not math.isfinite(numeric_credits) or numeric_credits <= 0:
        raise ValueError("credits must be positive")


def calculate_cgpa(courses: Iterable[tuple[str, float]]) -> float:
    """Return the credit-weighted CGPA rounded to 2 decimals.

    Args:
        courses: iterable of ``(grade, credits)`` pairs, e.g. ``("A", 4)``.

    Raises:
        ValueError: if empty, a grade is unknown, or credits are not positive.
    """
    scale = load_grade_scale()
    courses = list(courses)
    if not courses:
        raise ValueError("courses must not be empty")
    total_points = total_credits = 0.0
    for grade, credits in courses:
        _validate(grade, credits, scale)
        total_points += scale[grade] * credits
        total_credits += credits
    return round(total_points / total_credits, 2)


def performance_band(cgpa: float) -> str:
    """Classify a CGPA into a performance band."""
    if not 0 <= cgpa <= 10:
        raise ValueError("cgpa must be between 0 and 10")
    if cgpa >= 8.5:
        return "Distinction"
    if cgpa >= 7.0:
        return "First Class"
    if cgpa >= 6.0:
        return "Second Class"
    if cgpa >= 4.0:
        return "Pass"
    return "Fail"
