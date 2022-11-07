#! /usr/bin/python

from bitcoin.rpc import RawProxy
import sys

p = RawProxy()

def getDecodedTx(txid):
    # First, retrieve the raw transaction in hex
    raw_tx = p.getrawtransaction(txid)
    # Decode the transaction hex into a JSON object
    decoded_tx = p.decoderawtransaction(raw_tx)
    # Return JSON
    return decoded_tx

def calcTxFee():
    tx_vout = 0
    tx_vin = 0
    decoded_tx = getDecodedTx(sys.argv[1])
    # First, sum all the vouts of the transaction
    for output in decoded_tx['vout']:
        tx_vout += output['value']

    # Now add every amount of vout nested in vin, with the index of outer vout
    for input in decoded_tx['vin']:
        new_tx = getDecodedTx(input['txid'])
        n = input['vout']
        tx_vin += new_tx['vout'][n]['value']

    print("Sum of all outputs:", tx_vout)
    print("Sum of all inputs:", tx_vin)
    print("Transaction fee:", tx_vin - tx_vout)

def main(): 
    calcTxFee()

main()
