import base64

# Input data
input_data = b'Hello, World!'

# Encode the input data to base64
base64_representation = base64.b64encode(input_data)

# Print the base64 representation
print(base64_representation.decode('utf-8'))
