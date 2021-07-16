from numpy import byte


class parameters: # Can touch theses
    RANDOMX_ARGON_MEMORY: int = 262144
    RANDOMX_ARGON_ITERATIONS: int = 3
    RANDOMX_ARGON_LANES: int = 1
    RANDOMX_ARGON_SALT = "RandomX\x03"
    RANDOMX_SUPERSCALAR_LATENCY: int = 170
    RANDOMX_DATASET_BASE_SIZE: int = 2147483648
    RANDOMX_DATASET_EXTRA_SIZE: int = 33554368
    RANDOMX_PROGRAM_SIZE: int = 256
    RANDOMX_PROGRAM_ITERATIONS: int = 2048
    RANDOMX_SCRATCHPAD_L3: int = 2097152
    RANDOMX_SCRATCHPAD_L2: int = 262144
    RANDOMX_SCRATCHPAD_L1: int = 16384

    # theses are all 8
    RANDOMX_CACHE_ACCESSES: int = 8
    RANDOMX_PROGRAM_COUNT: int = RANDOMX_CACHE_ACCESSES
    RANDOMX_JUMP_BITS: int = RANDOMX_CACHE_ACCESSES
    RANDOMX_JUMP_OFFSET: int = RANDOMX_CACHE_ACCESSES

class keys: # Don't fucking touch theses
    class AesGenerator1R:
        key0: str = b"53 a5 ac 6d 09 66 71 62 2b 55 b5 db 17 49 f4 b4"
        key1: str = b"07 af 7c 6d 0d 71 6a 84 78 d3 25 17 4e dc a1 0d"
        key2: str = b"f1 62 12 3f c6 7e 94 9f 4f 79 c0 f4 45 e3 20 3e"
        key3: str = b"35 81 ef 6a 7c 31 ba b1 88 4c 31 16 54 91 16 49"
        total: list = [key0,key1,key2,key3]