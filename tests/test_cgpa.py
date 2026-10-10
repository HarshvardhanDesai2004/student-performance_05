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


@pytest.mark.parametrize(
    "courses, expected",
    [
        ([("A", 4)], 8.0),
        ([("O", 4), ("B", 2)], 8.67),
        ([("A+", 3), ("F", 3)], 4.5),
    ],
)
def test_valid_cgpa_calculations(courses, expected):
    assert calculate_cgpa(courses) == expected


def test_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_cgpa([])


@pytest.mark.parametrize("grade", [None, 1, 3.14, True, object()])
def test_non_string_grade_raises(grade):
    with pytest.raises(ValueError):
        calculate_cgpa([(grade, 3)])


def test_invalid_grade_raises():
    with pytest.raises(ValueError):
        calculate_cgpa([("Z", 3)])


@pytest.mark.parametrize("credits", [True, False, "3", object(), None])
def test_non_numeric_or_boolean_credits_raises(credits):
    with pytest.raises(ValueError):
        calculate_cgpa([("A", credits)])


@pytest.mark.parametrize("credits", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_credits_raises(credits):
    with pytest.raises(ValueError):
        calculate_cgpa([("A", credits)])


def test_non_positive_credits_raises():
    with pytest.raises(ValueError):
        calculate_cgpa([("A", 0)])


@pytest.mark.parametrize(
    ("cgpa", "band"),
    [
        (9.0, "Distinction"),
        (8.5, "Distinction"),
        (7.2, "First Class"),
        (6.0, "Second Class"),
        (4.0, "Pass"),
        (3.9, "Fail"),
    ],
)
def test_performance_band(cgpa, band):
    from student_performance.cgpa import performance_band

    assert performance_band(cgpa) == band


@pytest.mark.parametrize("bad", [-0.1, 10.1])
def test_performance_band_out_of_range(bad):
    from student_performance.cgpa import performance_band

    with pytest.raises(ValueError):
        performance_band(bad)
