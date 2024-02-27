import uuid

def generate_unique_id():
    return str(uuid.uuid4())

# Example usage:
unique_id = generate_unique_id()
print("Unique ID:", unique_id)
