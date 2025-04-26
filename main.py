from concrete import fhe

def add(x, y):
    return x + y

compiler = fhe.Compiler(add, {"x": "encrypted", "y": "encrypted"})

inputset = [(5, 5), (0, 0), (5, 6)]

print(f"Compilation...")
circuit = compiler.compile(inputset)
print(circuit)

print(f"Key generation...")
circuit.keygen()

encrypted_x, encrypted_y = circuit.encrypt(5, 5)
print(f'Encrypted x: {encrypted_x}')
print(f'Encrypted y: {encrypted_y}')

encrypted_result = circuit.run(encrypted_x, encrypted_y)
print(f"Encrypted result: {encrypted_result}")

result = circuit.decrypt(encrypted_result)
print(f"Decrypted result: {result}")

assert result == add(5, 5)