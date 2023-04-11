import pytest

from scripts.phonebook import search_core, search_phonenumber


@pytest.mark.parametrize(
    "phonebook, reference_name, expected",
    [
        (
            [
                {"555-555-5555": "Bill Gates"},
                {"111-555-5555": "Elon Musk"},
                {"222-555-5555": "John Doe"},
                {"222-555-5555": "Steven Jobs"},
            ],
            "BILL GATES",
            "555-555-5555",
        ),
        (
            [
                {"555-555-5555": "Bill Gates"},
                {"111-555-5555": "Elon Musk"},
                {"222-555-5555": "John Doe"},
                {"222-555-5555": "Steven Jobs"},
            ],
            "Steven Cliton",
            None,
        ),
    ],
)
def test_search_phonenumber(phonebook, reference_name, expected):
    """Unit test for search_phonenumber function"""
    result = search_phonenumber(phonebook, reference_name)
    assert result == expected


@pytest.mark.parametrize(
    "phonebook, contact_list, reference_name, begin, end, expected",
    [
        (
            [
                {"555-555-5555": "Bill Gates"},
                {"111-555-5555": "Elon Musk"},
                {"222-555-5555": "John Doe"},
                {"222-555-5555": "Steven Jobs"},
            ],
            ["Bill Gates", "Elon Musk", "John Doe", "Steven Jobs"],
            "BILL GATES",
            0,
            None,
            "555-555-5555",
        ),
        (
            [
                {"555-555-5555": "Bill Gates"},
                {"111-555-5555": "Elon Musk"},
                {"222-555-5555": "John Doe"},
                {"222-555-5555": "Steven Jobs"},
            ],
            ["Bill Gates", "Elon Musk", "John Doe", "Steven Jobs"],
            "Steven Cliton",
            1,
            3,
            None,
        ),
    ],
)
def test_search_core(
    phonebook, contact_list, reference_name, begin, end, expected
):
    """Unit test for search_core function"""
    result = search_core(phonebook, contact_list, reference_name, begin, end)
    assert result == expected
