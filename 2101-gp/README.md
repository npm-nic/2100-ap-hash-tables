# Hash Tables (2101)

- Recorded Lecture [here](https://www.youtube.com/watch?v=4TXTLaQqu6s&feature=youtu.be)
- Beej's notes [here](hash.py)

---

## Hash Table Operations

PUT

- operation to store something in a hash table
- takes the same amount of time no matter how many items are in the array
- GOAL: be able to search through array and see if its in there and have it always be constant time complexity o(1)

```python
def put(key, value):
  index = get_index(key)
  table[index] = HashEntry(key, value)
```

❓ How can put be o(1) if it uses get_index() that uses hashf() that uses a for loop? ❓

- hashf() is o(n) for the length of the key
- it is _NOT_ o(n) for the number of items in the list
- at no point is there something that goes through each item in the table
  - O(n) over the length (number of bytes) of the key
  - O(1) over the number of items in the table

GET

```python
def get(key):
  index = get_index(key)
  hash_entry = table[index]

  return hash_entry.value
```

---

## XOR

^ --> XOR

- bitwise operation that operates on numbers one bit at a time and comes up with a result
- if either of the bits are on, but not both of them, it returns a 1
- otherwise, the result is zero
- more on this in computer architecture sprint

---

## Bonus Information from Lecture

- Beej's notes [here](hash_updated.py)

python doesn't care how big the number is

- use 32 or 64-bit hash in `hashf()` to clamp size of number to 32 or 64 bits, respectively

```python
  # 32-bit hash
  total &= 0xffffffff
  # same as ⬇️
  total %= 0x100000000
```

- it will work if you do not do this, but it may run incorrectly or run into issues
