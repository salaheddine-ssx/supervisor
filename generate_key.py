#!/usr/local/bin/python
from cryptography.fernet import Fernet
print Fernet.generate_key()
