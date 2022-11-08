#! /usr/bin/python

from bitcoin.rpc import RawProxy
from binascii import unhexlify, hexlify
import hashlib, struct, sys, re

p = RawProxy()


def calcLittleEndian(num):
    return hexlify(struct.Struct('<L').pack(num))

def hashToHex(string):
    return hexlify(bytes.fromhex(string)[::-1])

def concatHash(block):
    prevhash = hashToHex(block["previousblockhash"])
    merkle = hashToHex(block["merkleroot"])
    nonce = calcLittleEndian(block["nonce"])
    time = calcLittleEndian(block["time"])
    version = calcLittleEndian(block["version"])
    bits = hashToHex(block["bits"])

    concatHex = version + prevhash + merkle + time + bits + nonce

    print("All components concatanated into single hex string:")
    print(concatHex)

    return unhexlify(concatHex)

# from wiki
# https://en.bitcoin.it/wiki/Block_hashing_algorithm
def validateHash(block):
    header_bin = concatHash(block)
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    hexlify(hash).decode("utf-8")
    blockhash = hexlify(hash[::-1]).decode("utf-8")
    validationRes = "- hash calculated correctly" if blockhash == block["hash"] else "- hash calculated incorrectly"
    print("Final hash:", blockhash, validationRes)

def main():
    hashPattern = "[0-9a-f]{64}"
    if(re.match(hashPattern,sys.argv[1])):
        block = p.getblock(sys.argv[1])
        validateHash(block)
    else:
        print("Wrong hash format")
        sys.exit()
main()
