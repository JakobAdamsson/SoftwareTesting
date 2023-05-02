"""
File written for an assignment in software testing where the purpose of the assignment was to test json libraries with fuzzing

Author: Jakob Adamsson
Acronym: jaad19
Student email: jaad19@student.bth.se
"""

import random
import time


def random_json_string() -> str:
    """Generate a random string with letters and digits. Always starting with a letter

    Returns:
        str: A random string
    """
    letters = [chr(i) for i in range(97, 123)]
    numbers = [str(i) for i in range(0, 10)]
    return "".join(random.choice(letters + numbers) for _ in range(random.randint(0, 100)))


def random_json_number() -> int:
    """Generate a random number

    Returns:
        int: A random int
    """
    return random.randint(0, 1000000)


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
    return {random_json_string(): random_json_string() for _ in range(random.randint(0, 100))}


def random_object_number() -> dict:
    """Generate a random object with random numbers

    Returns:
        dict: A dictionary with random numbers
    """
    return {random_json_string(): random_json_number() for _ in range(random.randint(0, 100))}


def random_nested_array() -> list:
    """Generate a random nested array

    Returns:
        list: A list of random json data
    """
    return [random.choice([random_json_string(), random_json_number(), random_boolean(), random_json_null()]) for _ in range(random.randint(0, 100))]


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
    print(f"Random number for dict: {nbr_of_json_objects}")

    randomized_json_list = []
    for _ in range(nbr_of_json_objects):
        random.seed(time.time())

        random_value_function = random.choice([
            random_json_string,
            random_json_number,
            random_json_float,
            random_boolean,
            random_json_null,
            random_nested_array
        ])

        # Generate a unique key and the value
        key = random_json_string()
        value = random_value_function()

        # Loop until we have a unique key
        while key in randomized_json_list:
            key = random_json_string()

        randomized_json_list.append({key: value})

    return randomized_json_list


def random_data_generator() -> None:
    random.seed(time.time())
    json_list = random_list_generator(1000)
    for json_object in json_list:
        print(json_object)
        yield json_object
