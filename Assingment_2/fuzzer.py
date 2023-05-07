import random

import json
import orjson
import msgspec
import time
from fuzzing_json import random_data_generator
from tqdm import tqdm
import ast  # To handle large numbers


def clear_file() -> None:
    """
    Function that clears the file
    """
    with open("mismatches.txt", "w") as f:
        f.write("")
    with open("exeptions.txt", "w") as f:
        f.write("")


def write_to_file(
    lib1: str = None,
    lib2: str = None,
    data: dict = None,
    lib1_encode=None,
    lib2_encode=None,
    exeption: str = None,
) -> None:
    """
    Writes content to file
    """
    if not exeption:
        with open("mismatches.txt", "a") as f:
            if not exeption:
                f.write(
                    f'{"="*150}\n{lib1} and {lib2} mismatch on data: {data}\n{lib1}encode: {lib1_encode}\n{lib2}encode: {lib2_encode} \n{"="*150}'
                )
    else:
        with open("exeptions.txt", "a") as f:
            f.write(
                f'{"="*150}\nExeption: {exeption}\nData that could not be encoded:\n{data}{"="*150}\n'
            )


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
            output_json = json.dumps(data, indent=None, separators=(",", ":"))
            # Try to encode with orjson
            output_orjson = orjson.dumps(data)

            # Try to encode with msgspec
            output_mesgspec = msgspec.json.encode(data)

        # If there is an exception, add it to the list of exceptions
        except Exception as exception:
            exeptions += [(exception, data)]
            write_to_file(exeption=exception, data=data)

        # If there is no exception, check if the outputs are the same for all the libraries
        else:
            decoded_output_json = output_json.encode().decode("utf-8")
            decoded_output_orjson = output_orjson.decode("utf-8")
            decoded_output_mesgspec = output_mesgspec.decode("utf-8")

            if not (
                decoded_output_json == decoded_output_orjson == decoded_output_mesgspec
            ):
                if not decoded_output_json == decoded_output_orjson:
                    write_to_file(
                        "json", "orjson", data, output_json.encode(), output_orjson
                    )
                if not decoded_output_json == decoded_output_mesgspec:
                    write_to_file(
                        "json", "msgspec", data, output_json.encode(), output_mesgspec
                    )
                if not decoded_output_orjson == decoded_output_mesgspec:
                    write_to_file(
                        "orjson", "msgspec", data, output_orjson, output_mesgspec
                    )
                mismatches += [data]
    print(f"{len(exeptions)} exceptions and {len(mismatches)} mismatches found")


if __name__ == "__main__":
    main()
