import pytest
from scripts.palindrome import is_palindrome


@pytest.mark.parametrize('text, expected',[
    ("HANNAH", "Yes"),
    ("GAGA", "No")
])
def test_is_palindrome(text, expected):
    """Unit test for is_palindrome function"""
    result = is_palindrome(text)
    assert result == expected
