import sys
from typing import Dict, List, Optional


def search_phonenumber(
    phonebook: List[Dict], reference_name: str
) -> Optional[str]:
    """If find the name on the list, it will get and return the contact number.
    Args:
        phonebook (List[Dict]):Phonebook Dict contacts or Phonebook contact dictonary
        reference_name (str): Reference name
    Returns:
        Optional[str]: return from search_core function
    """
    contacts = []
    for contact in phonebook:
        for number, name in contact.items():
            contacts.append(name)
    return search_core(phonebook, contacts, reference_name)


def search_core(
    phonebook: List[Dict],
    contact_list: List[str],
    name: str,
    begin: int = 0,
    end: Optional[int] = None,
) -> Optional[str]:
    """Simple binary search engine for phone book

    Args:
        phonebook (List[Dict]): phonebook agenda list
        contact_list (List[str]): contact list reference
        name (str): reference name to search
        begin (int, optional): Index to start. Defaults to 0.
        end (Optional[int], optional): Index to finish. Defaults to None.

    Returns:
        Optional[str]: Return the result on the contact number or none, if not found!
    """
    length = len(contact_list)
    if end is None:
        end = length - 1

    while begin <= end:
        middle = (begin + end) // 2
        if contact_list[middle].lower() == name.lower():
            return list(phonebook[middle].keys())[0]
        elif contact_list[middle].lower() != name.lower():
            end = middle - 1
        else:
            begin = middle - 1
    return None


if __name__ == "__main__":
    # You are expected to receive a list of contacts according to the statement in the spefic format!
    print(
        f"{sys.argv[2]}'s phone number is : {search_phonenumber(sys.argv[1], sys.argv[2])}"
    )
