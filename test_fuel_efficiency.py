"""
Test methods for Fuel Efficiency program
"""

from fuel_efficiency import calculate_mpg, categorize_efficiency


def test_calculate_mpg_with_100_distance_and_5_fuel():
    """
    Test for calculation of MPG where 5 gallons resulted in 100 miles
    """
    assert calculate_mpg(100, 5) == 20.0


def test_calculate_mpg_with_150_distance_and_7_5_fuel():
    """
    Test for calculation of MPG where 6 gallons resulted in 150 miles
    """
    assert calculate_mpg(150, 6) == 25.0


def test_categorize_efficiency_very_poor():
    """
    Test for very poor fuel efficiency
    """
    assert categorize_efficiency(10) == "very poor"


def test_categorize_efficiency_poor():
    """
    Test for poor fuel efficiency
    """
    assert categorize_efficiency(16) == "poor"


def test_categorize_efficiency_average():
    """
    Test for average fuel efficiency
    """
    assert categorize_efficiency(25) == "average"


def test_categorize_efficiency_good():
    """
    Test for good fuel efficiency
    """
    assert categorize_efficiency(35) == "good"


def test_categorize_efficiency_excellent():
    """
    Test for excellent fuel efficiency
    """
    assert categorize_efficiency(50) == "excellent"
