# CryptoJsAes Python Library

This Python library is a rewritten version of the CryptoJS AES library in PHP. It allows you to encrypt and decrypt data using the AES algorithm.

## Usage

### Encryption

To encrypt data, you can use the `encrypt(data, password)` method. The `data` parameter can be a dictionary or a string, and the `password` parameter is the password you want to use for encryption.

Example:

```python
import CryptoJsAes

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
{"ct": "uWxBJw3yviWkUg==", "iv": "1f5b28b8f7a3d87fc4e37d0dc8c3f1e3", "s": "f6e1c3fcd7e8a0f0"}
```

### Decryption

To decrypt data, you can use the `decrypt(json_str, password)` method. The `json_str` parameter is the encrypted data in JSON format, and the `password` parameter is the password used for encryption.

Example:

```python
import CryptoJsAes

encrypted_data = '{"ct": "uWxBJw3yviWkUg==", "iv": "1f5b28b8f7a3d87fc4e37d0dc8c3f1e3", "s": "f6e1c3fcd7e8a0f0"}'
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
