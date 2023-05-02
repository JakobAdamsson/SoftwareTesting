import random

import json
import orjson
import msgspec
import time

from tqdm import tqdm


def random_data_generator() -> None:
    """
    Function that generates random data with yeild
    Yield creates a generator, which is a function that can be called multiple times

    Yields:
        Iterator[dict]: A dictionary with two fields, each with a random integer
        A generator is created each time this function is called
    """
    while True:
        yield {'field_1': random.randint(0, 100),
               'field_2': random.randint(100, 200)}  # maybe you have a better idea


def main() -> None:
    # Set random seed
    random.seed(time.time())
    # Returns dict with two fields, each with a random integer
    data_generator = random_data_generator()
    exeptions = []
    mismatches = []
    for _ in tqdm(range(1000)):
        # Get next data (since its a generator, it will be different each time)
        data = next(data_generator)
        print(data)
        try:
            # Try to encode data with each library
            # Try to encode with json
            output_json = json.dumps(data, indent=None,
                                     separators=(',', ':'))
            # Try to encode with orjson
            output_orjson = orjson.dumps(data)

            # Try to encode with msgspec
            output_mesgspec = msgspec.json.encode(data)

        # If there is an exception, add it to the list of exceptions
        except Exception as exception:
            exeptions += [(exception, data)]

        # If there is no exception, check if the outputs are the same for all the libraries
        else:
            if not output_json.encode() == output_orjson == output_mesgspec:
                print(output_json.encode(), output_orjson, output_mesgspec)
                mismatches += [data]
    print(f'{len(exeptions)} exceptions and {len(mismatches)} mismatches found')


if __name__ == '__main__':
    main()
