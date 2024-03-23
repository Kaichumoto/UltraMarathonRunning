# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def convert_to_km(distance_str):
    """
    This function converts a distance string (e.g., "6km", "3mi") to kilometers.

    Args:
        distance_str: The string representation of the distance.

    Returns:
        The distance in kilometers as a float.
    """
    unit = distance_str[-2:]  # Get the last two characters (units)
    value = float(distance_str[:-2])  # Extract the numerical value

    if unit == "km":
        return value
    elif unit == "mi":
        # 1 mile = 1.60934 kilometers
        return value * 1.60934
    else:
        raise ValueError(f"Unknown unit: {unit}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('DataSpell')
    print(convert_to_km('105.6km'))

# See DataSpell help at https://www.jetbrains.com/help/dataspell/
  
#%%
