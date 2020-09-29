table = [None] * 8

class HashEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __repr__(self):
		return f"HashEntry({repr(self.key)},{repr(self.value)})"

def hashf(s):
	"""Naive hashing function--do not use!"""
	total = 0

	bytes = str(s).encode()

	for b in bytes:  # O(n) over the length of the key/string s
		total += b

	return total

def get_index(s):
	value = hashf(s)

	return value % len(table)

def put(key, value):
	"""
	O(n) over the length (number of bytes) of the key
	O(1) over the number of items in the table
	"""
	index = get_index(key)
	table[index] = HashEntry(key, value)

def get(key):
	index = get_index(key)
	hash_entry = table[index]

	return hash_entry.value

put("Beej", 3490)

print(table)

put("Goats!", 9999)

print(table)

print(get("Beej"))  # 3490
print(get("Goats!"))  # 9999
