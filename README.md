# CryptoJsAes Python Library

This Python library is a rewritten version of the CryptoJS AES library in PHP. It allows you to encrypt and decrypt data using the AES algorithm.

## Usage

### Encryption

To encrypt data, you can use the `encrypt(data, password)` method. The `data` parameter can be any type, and the `password` parameter is the password you want to use for encryption.

Example:

```python
from CryptojsAesPython import CryptoJsAes

data = {
    "username": "john_doe",
    "password": "secretpassword"
}

password = "mysecretpassword"

encrypted_data = CryptoJsAes.encrypt(data, password)
print(encrypted_data)
```

Output:

```
{"ct": "KXaW9CEDgQlr9sN/fp8/E4jsRpFeF8/pdocrsaQ8PdnSSJp1e5kIwD3nrNS8gBzcp5h+no/KVxTNppjHwa9U9A==", "iv": "0e944c921ea2baad50091a2ee2c3aba9", "s": "af31ce71841c9620"}
```

### Decryption

To decrypt data, you can use the `decrypt(json_str, password)` method. The `json_str` parameter is the encrypted data in JSON format, and the `password` parameter is the password used for encryption.

Example:

```python
from CryptojsAesPython import CryptoJsAes

encrypted_data = '{"ct": "KXaW9CEDgQlr9sN/fp8/E4jsRpFeF8/pdocrsaQ8PdnSSJp1e5kIwD3nrNS8gBzcp5h+no/KVxTNppjHwa9U9A==", "iv": "0e944c921ea2baad50091a2ee2c3aba9", "s": "af31ce71841c9620"}'
password = "mysecretpassword"

decrypted_data = CryptoJsAes.decrypt(encrypted_data, password)
print(decrypted_data)
```

Output:

```
{'username': 'john_doe', 'password': 'secretpassword'}
```

## Credits

This Python library is a rewritten version of the CryptoJS AES library in PHP, originally developed by brainfoolong. The original PHP code can be found at [https://github.com/brainfoolong/cryptojs-aes-php](https://github.com/brainfoolong/cryptojs-aes-php).

## License

This library is licensed under the [MIT License](https://opensource.org/licenses/MIT).
