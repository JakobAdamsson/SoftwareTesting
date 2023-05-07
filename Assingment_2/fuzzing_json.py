"""
File written for an assignment in software testing where the purpose of the assignment was to test json libraries with fuzzing

Author: Jakob Adamsson
Acronym: jaad19
Student email: jaad19@student.bth.se
"""

# Imports
import random
import time
import sys


def random_letter_from_unicode_block(range_s: int, range_e: int) -> str:
    """A function that returns a random letter from a unicode block using chr

    Args:
        range_s (int): Start of the unicode block
        range_e (int): End of the unicode block

    Returns:
        str: A random letter from the unicode block within range_s and range_e
    """
    return chr(random.randint(range_s, range_e))


def random_list_nested_generator(current_depth=0, max_depth=5) -> list:
    if current_depth >= max_depth:
        return random.choice(
            [
                random_json_string(),
                random_json_number(),
                random_json_float(),
                random_boolean(),
                random_json_null(),
                random_json_large_float(),
                random_json_large_number(),
                random_json_small_number(),
                random_json_small_float(),
                random_json_unicode_string(),
            ]
        )

    structure_type = random.choice(["list", "dict"])

    if structure_type == "list":
        nested_list = [
            random_list_nested_generator(current_depth + 1, max_depth)
            for _ in range(random.randint(1, 5))
        ]
        return nested_list

    elif structure_type == "dict":
        nested_dict = {
            random_json_string(): random_list_nested_generator(
                current_depth + 1, max_depth
            )
            for _ in range(random.randint(1, 5))
        }
        return nested_dict


def random_json_unicode_string() -> str:
    """Generates a random unicode string
    Informarion about the different unicode characters are gathered from: https://en.wikipedia.org/wiki/Latin_script_in_Unicode

    Returns:
        str: String with unicode characters
    """
    unicode_blocks = [
        ("Basic Latin", 0x0000, 0x007F),
        ("Latin-1 Supplement", 0x0080, 0x00FF),
        ("Latin Extended-A", 0x0100, 0x017F),
        ("Latin Extended-B", 0x0180, 0x024F),
        ("IPA Extensions", 0x0250, 0x02AF),
        ("Spacing Modifier Letters", 0x02B0, 0x02FF),
        ("Phonetic Extensions", 0x1D00, 0x1D7F),
        ("Phonetic Extensions Supplement", 0x1D80, 0x1DBF),
        ("Latin Extended Additional", 0x1E00, 0x1EFF),
        ("Superscripts and Subscripts", 0x2070, 0x209F),
        ("Letterlike Symbols", 0x2100, 0x214F),
        ("Number Forms", 0x2150, 0x218F),
        ("Latin Extended-C", 0x2C60, 0x2C7F),
        ("Latin Extended-D", 0xA720, 0xA7FF),
        ("Latin Extended-E", 0xAB30, 0xAB6F),
        ("Alphabetic Presentation Forms (Latin ligatures)", 0xFB00, 0xFB4F),
        ("Halfwidth and Fullwidth Forms", 0xFF00, 0xFFEF),
        ("Latin Extended-F", 0x10780, 0x107BF),
        ("Latin Extended-G", 0x1DF00, 0x1DFFF),
    ]
    lenght_of_string = random.randint(1, 100)
    unicoded_string = ""
    for _ in range(lenght_of_string):
        blockname, range_s, range_e = random.choice(unicode_blocks)
        random_letter = random_letter_from_unicode_block(range_s, range_e)
        unicoded_string = unicoded_string + random_letter
    return unicoded_string


def random_json_string() -> str:
    """Generate a random string with letters and digits. Always starting with a letter

    Returns:
        str: A random string
    """
    letters = [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(0, 10)]
    return "".join(
        random.choice(letters + numbers) for _ in range(random.randint(0, 100))
    )


def random_json_number() -> int:
    """Generate a random number

    Returns:
        int: A random int
    """
    return random.randint(0, 1000000)


def random_json_large_number() -> int:
    """Generate a large random number

    Returns:
        int: A random large int
    """
    return random.randint(sys.maxsize - 100, sys.maxsize)


def random_json_small_number() -> int:
    """Generate a small random number

    Returns:
    int: A random small int
    """
    return random.randint(sys.maxsize, sys.maxsize * 100)


def random_json_large_float() -> float:
    """Generate a large random float

    Returns:
    int: A random large float
    """
    random_float = random.uniform(sys.float_info.max / 100, sys.float_info.max)
    if "+" in str(random_float):
        random_float = str(random_float).replace("+", "")
        return random_float
    return random_float


def random_json_small_float() -> float:
    """Generate a small random float

    Returns:
    int: A random small float
    """
    return random.uniform(sys.float_info.min, sys.float_info.min * 100)


def random_json_float() -> float:
    """Generate a random float

    Returns:
        float: A random float
    """
    return random.random()


def random_boolean() -> bool:
    """Generate a random boolean

    Returns:
        bool: A random boolean(True, False)
    """
    return random.choice([True, False])


def random_json_null() -> None:
    """Generate a random null value

    Returns:
        _type_: A null value
    """
    return None


def random_object_string() -> dict:
    """Generate a random object with random strings

    Returns:
        dict: A dictionary with random strings
    """
    return {
        random_json_string(): random_json_string()
        for _ in range(random.randint(0, 100))
    }


def random_object_number() -> dict:
    """Generate a random object with random numbers

    Returns:
        dict: A dictionary with random numbers
    """
    return {
        random_json_string(): random_json_number()
        for _ in range(random.randint(0, 100))
    }


def random_nested_array() -> list:
    """Generate a random nested array

    Returns:
        list: A list of random json data
    """
    return [
        random.choice([random_json_unicode_string()])
        for _ in range(random.randint(0, 100))
    ]


def random_list_generator(nbr_of_json_objects: int) -> list:
    """
    A method that generates random data that can be used to test the json libraries
    The function will yield back the result to be tested in fuzzer.py

    JSON examples used from https://www.microfocus.com/documentation/silk-performer/195/en/silkperformer-195-webhelp-en/GUID-6AFC32B4-6D73-4FBA-AD36-E42261E2D77E.html

    A json object looks like this:
    json_data_types = {
        "StringProperty": "string",
        "NumberProperty": 123,
        "FloatProperty": 123.456,
        "BooleanProperty": True,
        "EmptyProperty": None,
        "NestedObject": {"Name": "Nested Object"},
        "NestedArray": [10, 20, True, "Nested Array"]
    }
    """
    print(f"Objects being generated -> {nbr_of_json_objects}")

    randomized_json_list = []
    randomized_list = []
    for _ in range(nbr_of_json_objects):
        random.seed(time.time())

        random_value_function = random.choice(
            [
                random_json_string,
                random_json_number,
                random_json_float,
                random_boolean,
                random_json_null,
                random_nested_array,
                random_json_large_float,
                random_json_large_number,
                random_json_small_number,
                random_json_small_float,
                random_json_unicode_string,
                random_list_nested_generator,
            ]
        )

        # Generate a unique key and the value
        key = random_json_string()
        value = random_value_function()

        # Loop until we have a unique key
        while key in randomized_json_list:
            key = random_json_string()

        randomized_json_list.append({key: value})
        randomized_list.append(value)

    return randomized_json_list, randomized_list


def random_data_generator() -> None:
    random.seed(time.time())
    json_list, random_list = random_list_generator(10000)
    joined_lits = json_list + random_list
    for item in joined_lits:
        yield item
