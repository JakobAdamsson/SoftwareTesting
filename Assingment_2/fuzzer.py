import random

import json
import orjson
import msgspec
import time
from fuzzing_json import random_data_generator
from tqdm import tqdm


def clear_file() -> None:
    with open('mismatches.txt', 'w') as f:
        f.write('')


def write_to_file(lib1: str, lib2: str, data: dict, lib1_endcode, lib2_encode) -> None:
    with open('mismatches.txt', 'a') as f:
        f.write(
            f'{"="*150}\n{lib1} and {lib2} mismatch on data: {data}\n{lib1}encode: {lib1_endcode}\n{lib2}encode: {lib2_encode} \n{"="*150}')


def main() -> None:
    # Clear file
    clear_file()
    # Set random seed
    random.seed(time.time())
    # Returns dict with two fields, each with a random integer
    data_generator = random_data_generator()
    exeptions = []
    mismatches = []
    for _ in tqdm(range(10000)):
        # Get next data (since its a generator, it will be different each time)
        data = next(data_generator)
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
            with open('exceptions.txt', 'a') as file:
                file.write(f'{exception} {data}\n')

        # If there is no exception, check if the outputs are the same for all the libraries
        else:
            if not output_json.encode() == output_orjson == output_mesgspec:
                if not output_json.encode() == output_orjson:
                    write_to_file('json', 'orjson', data,
                                  output_json.encode(), output_orjson)
                if not output_json.encode() == output_mesgspec:
                    write_to_file('json', 'msgspec', data,
                                  output_json.encode(), output_mesgspec)
                if not output_orjson == output_mesgspec:
                    write_to_file('orjson', 'msgspec', data,
                                  output_orjson, output_mesgspec)
                    # print(output_json.encode(), output_orjson, output_mesgspec)
                mismatches += [data]
    print(f'{len(exeptions)} exceptions and {len(mismatches)} mismatches found')


if __name__ == '__main__':
    main()
