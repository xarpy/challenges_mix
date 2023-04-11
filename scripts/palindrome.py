import sys


def is_palindrome(text: str) -> str:
    """Simple function, reverse the text argment, and compare if
    is equal with than reversed!
    Args:
        text (str): Word to receive as argument.
    Returns:
        str: return status to show on terminal.
    """
    reverse_text = text[::-1]
    return "Yes" if reverse_text == text else "No"


if __name__ == "__main__":
    print(
        f"This result is answer for doubt if word is palindrome: {is_palindrome(sys.argv[1])}"
    )
