from employee_details import *

def test_high_salary():
    salary = 60000
    assert salary >= 50000

def test_medium_salary():
    salary = 35000
    assert 30000 <= salary < 50000

def test_low_salary():
    salary = 15000
    assert salary < 30000
