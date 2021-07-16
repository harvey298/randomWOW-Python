# Harvey298 GNU GPL3
import hashlib
from configuation import keys

def AesGenerator1R(key: int = 0):
    if key >= 4:
        return hashlib.blake2b(keys.AesGenerator1R.total[0], digest_size=64, key=b'', salt=b'', person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False).digest()
    else: return hashlib.blake2b(keys.AesGenerator1R.total[key], digest_size=64, key=b'', salt=b'', person=b'', fanout=1, depth=1, leaf_size=0, node_offset=0, node_depth=0, inner_size=0, last_node=False).digest()