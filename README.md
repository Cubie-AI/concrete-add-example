# FHE Add

Execute an add function by passing in encrypted parameters.

## Set up

```
python3 -m venv venv
source venv/bin/activate
pip install -r .
```

## Running

```
python main.py
```

## Sample Output

```
Compilation...
%0 = x                  # EncryptedScalar<uint3>        ∈ [0, 5]
%1 = y                  # EncryptedScalar<uint3>        ∈ [0, 6]
%2 = add(%0, %1)        # EncryptedScalar<uint4>        ∈ [0, 11]
return %2
Key generation...
Encrypted x: <concrete.fhe.compilation.value.Value object at 0x1285e14d0>
Encrypted y: <concrete.fhe.compilation.value.Value object at 0x12864af50>
Encrypted result: <concrete.fhe.compilation.value.Value object at 0x1285c8690>
Decrypted result: 10
```
