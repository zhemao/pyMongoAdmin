# WWBFAQIAAUTS - What would be Frequently Asked Questions if Anyone Actually Used This Software

## How do I manage users?

Anaconda users are simply documents in the users collection in the anaconda database.
Each document has a username field, and a password field which stores a sha256 hash
of the plaintext password. To add a new user with username `'username'` and password
`'password'` put `'username'` in the username field and `sha256('password')` in the password field. These are just examples, please don't actually create a user with 
this exact username and password. To change a user's password, just enter in 
`sha256('newpassword')`.

## How do I add a new database or a new collection

MongoDB adds a database or collection when the first document is inserted into
the database or collection. To put in the first document, use the form in the
[list of databases](../) or [list of collections](../db/anaconda) that says 
"Add new document". 
