# Copyright (c) 2023, Nick Shepherd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import binascii
import pathlib

def generate_aes_key():
    key = os.urandom(32)
    return key


def generate_des_key():
    key = os.urandom(8)
    return key


def convert_to_hex(key):
    hex_key = binascii.hexlify(key).decode('utf-8')
    return hex_key


def save_to_file(key, filename):
    with open(filename, 'w') as file:
        file.write(key)


def main():
    choice = input("Choose encryption algorithm ([1] for AES, [2] for DES): ")

    if choice == "1":
        key = generate_aes_key()
        encryption_algorithm = "AES"
    elif choice == "2":
        key = generate_des_key()
        encryption_algorithm = "DES"
    else:
        print("Invalid choice. Please choose either 1 for AES or 2 for DES.")
        return

    hex_key = convert_to_hex(key)

    downloads_folder = pathlib.Path.home() / "Downloads"
    filename = f"{encryption_algorithm}_key.txt"
    filepath = downloads_folder / filename
    save_to_file(hex_key, filepath)

    print(f"Key saved to: {filepath}")


if __name__ == "__main__":
    main()
