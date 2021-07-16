# Harvey298 GNU GPL3

from AesGenerator1R import AesGenerator1R
import hashlib, numpy, math, time, threading, argon2

# Argon 2 Docs: https://argon2-cffi.readthedocs.io/en/stable/api.html

# Hashlib.blake2b Docs: https://docs.python.org/3/library/hashlib.html#hashlib.blake2b

# Wownero Documentation: https://git.wownero.com/wownero/RandomWOW/src/branch/1.1.9-wow/doc/specs.md#user-content-3-custom-functions

# Change the number here, cannot go above 3!
key = 0

print(AesGenerator1R(key))