import sys
from typing import List


def input_data() -> List[List[str]]:
    """Factory method to generate the array pixels"""
    return [
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", "#", "."],
        [".", "#", "#", "#", ".", "."],
        [".", "#", ".", ".", ".", "."],
    ]


def paint_bucket(
    image: List[List[str]], row: int, column: int, new_color: str
) -> List[List[str]]:
    """Main method, to validate the array of vectors.
    Args:
        image (List[List[str]]): image array characters
        row (int): The row position to change.
        column (int): The column position to change
        new_color (str): The new color to change.

    Returns:
        List[List[str]]: return the same image change or not, its depends tto the function core.
    """
    if image[row][column] == new_color:
        return image
    paint_core(image, row, column, image[row][column], new_color)
    return image


def paint_core(
    image: List[List[str]], row: int, column: int, color: str, new_color: str
):
    """Function paint core recursive, check if the color character is the same, if not execute the process.
    Args:
        image (List[List[str]]): image array characters
        row (int): The row position to change.
        column (int): The column position to change
        color (str): The old color to reference for verify
        new_color (str): The new color to change.
    """
    if image[row][column] == color:
        image[row][column] = new_color
        if row >= 1:
            paint_core(image, row - 1, column, color, new_color)
        if row + 1 < len(image):
            paint_core(image, row + 1, column, color, new_color)
        if column >= 1:
            paint_core(image, row, column - 1, color, new_color)
        if column + 1 < len(image[0]):
            paint_core(image, row, column + 1, color, new_color)


if __name__ == "__main__":
    # If you need to change the image array, just insert another character array in the input_data method!
    new_image = paint_bucket(
        input_data(), int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    )
    for item in new_image:
        print(*item)
