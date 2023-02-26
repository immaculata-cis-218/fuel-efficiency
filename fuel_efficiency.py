"""
Fuel Efficiency program
Andrew Bowman
"""


def calculate_mpg(miles: int, gallons: int) -> int:
    """
    Calculates the fuel efficiency in miles per gallon (mpg)
    """
    return miles / gallons


def categorize_efficiency(mpg: int) -> str:
    """
    Categorizes the fuel efficiency in miles per gallon (mpg) into different ratings.
    """

    if mpg < 15:
        return "very poor"
    if mpg < 20:
        return "poor"
    if mpg < 30:
        return "average"
    if mpg < 40:
        return "good"
    return "excellent"


if __name__ == "__main__":
    distance = float(input("Enter the distance traveled in miles: "))
    fuel = float(input("Enter the amount of fuel used in gallons: "))
    rating = calculate_mpg(distance, fuel)
    efficiency = categorize_efficiency(rating)
    print(f"Your car has {efficiency} fuel efficiency!")
