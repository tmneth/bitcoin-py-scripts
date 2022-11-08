### Get transaction fee from `getrawtransaction`

`./rpc_fee.py 4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d`

```
Sum of all outputs: 94504.03465148
Sum of all inputs: 94504.10000000
Transaction fee: 0.06534852
```

### Calculate and verify a hash of a block from `blockheader`

For example, let's consider Block#125,552

`./rpc_verify_hash.py 00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d`

```
All components concatanated into single hex string:
b'0100000081cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122bc7f5d74df2b9441a42a14695'

Final hash: 00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d is calculated correctly
```
