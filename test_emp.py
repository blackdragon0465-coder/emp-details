import pytest

from emp_details import salary_category


def test_high_salary():
    assert salary_category(60000) == "High Salary"


def test_medium_salary():
    assert salary_category(40000) == "Medium Salary"


def test_low_salary():
    assert salary_category(20000) == "Low Salary"


@pytest.mark.parametrize("salary, expected", [
    (50000, "High Salary"),
    (70000, "High Salary"),
    (30000, "Medium Salary"),
    (49999, "Medium Salary"),
    (25000, "Low Salary"),
    (0, "Low Salary"),
])
def test_salary_boundaries(salary, expected):
    assert salary_category(salary) == expected


def test_negative_salary():
    # Negative salary should still be considered Low Salary
    assert salary_category(-5000) == "Low Salary"


def test_very_high_salary():
    assert salary_category(1000000) == "High Salary"
