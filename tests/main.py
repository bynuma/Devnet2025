def calculate_rectangle_area(length, width):                                # This function calculates the area of a rectangle given its length and width.

    if length <= 0 or width <= 0:                                           # Check if either the length or width is not positive.
        raise ValueError("Length and width must be positive numbers")       # Raise a ValueError with a descriptive message.
    return length * width                                                   # Return the calculated area of the rectangle.

if __name__ == "__main__":                                  # Check if the script is being run directly.
    # Example usage
    try:                                                    # Use a try-except block to handle potential ValueErrors when calculating the area.
        length = 5
        width = 10
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    except ValueError as e:
        print(f"Error: {e}") 