# Mongoose Users' Manual

## Entering Data

Mongoose is written in python, and so the items in each document are entered
in python syntax.

### Datatypes

The following datatypes can be entered into document items

 * String - `'single quotes'` or `"double quotes"`
 * Integer - `1`, `2`, `3`
 * Float - `3.2`, `2.7e3`
 * Dictionary - `{'key':'val'}`
 * List - `['foo', 3, 2.0]`
 * ObjectId - `oid('4deba114d0eea90a0f000001')`
 * Datetime - `datetime(2011, 6, 5, 14, 15, 15, 276946)` 
 * Binary Data - `bin('\x3ekdk\x80')`
 * Compiled Regular Expression - `regex(r'\w+')`
 * Javascript Code - `code('alert();')`
 
### Methods

These methods are available for your use to make entering in data easier

 * now() - Get the current datetime.
 * sha256(plain) - Converts the plaintext `plain` into its sha256 hash. This is the hash function used by mongoose to store user passwords.
 * sha1(plain) - Converts the plaintext `plain` into its sha1 hash. 
 * md5(plain) - Converts the plaintext `plain` into its md5 hash.
 
You can also use any methods in the datetime and math libraries.

## Contact me

If you have any other questions about Mongoose that this documentation doesn't 
address, please send any queries to the author at zhehao.mao@gmail.com.
