#! /usr/bin/python

from bitcoin.rpc import RawProxy
import sys, re

p = RawProxy()

def getDecodedTx(txid):
    # First, retrieve the raw transaction in hex
    raw_tx = p.getrawtransaction(txid)
    # Decode the transaction hex into a JSON object
    decoded_tx = p.decoderawtransaction(raw_tx)
    # Return JSON
    return decoded_tx

def calcTxFee():
    total_vout = 0
    total_vin = 0
    decoded_tx = getDecodedTx(sys.argv[1])
    # First, sum all the vouts of the transaction
    for output in decoded_tx['vout']:
        total_vout += output['value']

    # Now add every amount of vout nested in vin, with the index of outer vout
    for input in decoded_tx['vin']:
        new_tx = getDecodedTx(input['txid'])
        tx_vout = input['vout']
        total_vin += new_tx['vout'][tx_vout]['value']

    print("Sum of all outputs:", total_vout)
    print("Sum of all inputs:", total_vin)
    print("Transaction fee:", total_vin - total_vout)

def main():
    hashPattern = "[0-9a-f]{64}"
    if(re.match(hashPattern,sys.argv[1])):
        calcTxFee()
    else:
        print("Wrong hash format")
        sys.exit()

main()
