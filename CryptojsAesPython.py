import base64
import hashlib
import json
import secrets

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad


class CryptoJsAes:
    @staticmethod
    def encrypt(data: dict or str, password: str) -> str:
        """
        Encrypt any value
        :param data: Value to be encrypted
        :param password: Your password
        :return: encrypted data
        :rtype: str
        """

        salt = bytes.fromhex(secrets.token_hex(8))
        iv = bytes.fromhex(secrets.token_hex(16))
        full_password = (password.encode() + salt)

        hashes_list = [hashlib.md5(full_password).digest()]
        result = hashes_list[0]
        i = 1

        while len(result) < 32:
            hashes_list.append(hashlib.md5(hashes_list[i - 1] + full_password).digest())
            result += hashes_list[i]
            i += 1

        key = result[:32]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(json.dumps(data).encode("utf-8"), AES.block_size))

        encrypted_json = {
            "ct": base64.b64encode(encrypted_data).decode("utf-8"),
            "iv": iv.hex(),
            "s": salt.hex()
        }

        return json.dumps(encrypted_json)

    @staticmethod
    def decrypt(json_str: str, password: str) -> list or dict or str:
        """
        Decrypt a previously encrypted value
        :param json_str: Json stringified value
        :param password: Your password
        :return: decrypted data
        :rtype: list or dict or str
        """

        json_data = json.loads(json_str)

        salt = bytes.fromhex(json_data["s"])
        iv = bytes.fromhex(json_data["iv"])
        encrypted_data = base64.b64decode(json_data["ct"])
        full_password = (password.encode() + salt)

        hashes_list = [hashlib.md5(full_password).digest()]
        result = hashes_list[0]
        i = 1

        while len(result) < 32:
            hashes_list.append(hashlib.md5(hashes_list[i - 1] + full_password).digest())
            result += hashes_list[i]
            i += 1

        key = result[:32]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        return json.loads(decrypted_data.decode("utf-8"))
