import crypt
salt = crypt.mksalt(crypt.METHOD_SHA256)
print(crypt.crypt("hello", salt))
