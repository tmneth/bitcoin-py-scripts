#! /usr/bin/python

from bitcoin.rpc import RawProxy
from binascii import unhexlify, hexlify
import hashlib
import struct
import sys

p = RawProxy()
block = p.getblock(sys.argv[1])

def calcLittleEndian(num):
    return hexlify(struct.Struct('<L').pack(num))

def hashToHex(string):
    return hexlify(bytes.fromhex(string)[::-1])

def concatHash():
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

# algo from wiki
# https://en.bitcoin.it/wiki/Block_hashing_algorithm
def validateHash():
    header_bin = concatHash()
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    hexlify(hash).decode("utf-8")
    blockhash = hexlify(hash[::-1]).decode("utf-8")
    validationRes = "- verified" if blockhash == block["hash"] else "- not verified"
    print("Final hash:", blockhash, validationRes)

def main():
    validateHash()

main()
