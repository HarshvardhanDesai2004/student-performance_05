"""Tests for CGPA calculation (AI-generated, human-reviewed)."""

import pytest

from student_performance.cgpa import calculate_cgpa


def test_single_course():
    assert calculate_cgpa([("A", 4)]) == 8.0


def test_credit_weighted_average():
    # (10*4 + 6*2) / 6 = 8.67
    assert calculate_cgpa([("O", 4), ("B", 2)]) == 8.67


def test_failed_course_credits_count():
    # (9*3 + 0*3) / 6 = 4.5
    assert calculate_cgpa([("A+", 3), ("F", 3)]) == 4.5


def test_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_cgpa([])


def test_invalid_grade_raises():
    with pytest.raises(ValueError):
        calculate_cgpa([("Z", 3)])


def test_non_positive_credits_raises():
    with pytest.raises(ValueError):
        calculate_cgpa([("A", 0)])
