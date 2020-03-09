import hashlib

n = 10
key = b"my_value" #b turns it in to byte array
key2 = "string1".encode() #so does this
key3 = "lunchtime".encode() #so does this

index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
print(index)
print(index2)
print(index3)


# for i in range (n):
#     print(hash(key))
#     print(hashlib.sha256(key).hexdigest())


# for i in range (n):
#     print(hash(key))
#
#
# for i in range (n):
#     print(hash(key2))
