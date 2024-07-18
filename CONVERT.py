import hashlib

class CONVERT_binhash:
    @staticmethod
    def convert(text, encoding):
        try:
            text = str(text)
            encoding = str(encoding)
        except TypeError:
            raise TypeError("text, encoding need to be string")

        convert = ''.join(format(ord(char), '08b') for char in text)

        if encoding in ("sha-1", "sha-256", "md5", "sha224", "sha384", "sha512"):  # Fixed the check for valid encodings
            Warn1 = input("THIS WILL BE UN-ERASABLE! TYPE Y TO CONTINUE, TYPE N, TO STOP!")
            if Warn1.upper() == "Y":
                print("Okay, converting!")
            elif Warn1.upper() == "N":
                exit("Exited!")
            else:
                raise TypeError("input has to be y or n")
        else:
            pass

        convert_encode = convert.encode('utf-8')

        hashed_data = None

        if encoding == "sha-1":
            hashed_data = hashlib.sha1(convert_encode).hexdigest()
        elif encoding == "sha-256":
            hashed_data = hashlib.sha256(convert_encode).hexdigest()
        elif encoding == "md5":
            hashed_data = hashlib.md5(convert_encode).hexdigest()
        elif encoding == "sha224":
            hashed_data = hashlib.sha224(convert_encode).hexdigest()
        elif encoding == "sha384":
            hashed_data = hashlib.sha384(convert_encode).hexdigest()
        elif encoding == "sha512":
            hashed_data = hashlib.sha512(convert_encode).hexdigest()
        elif encoding == "utf-16":
            convert_bytes = bytes(int(convert[i:i+8], 2) for i in range(0, len(convert), 8))
            utf16 = convert_bytes.decode('utf-8').encode('utf-16')
        else:
            raise TypeError("encoding must be sha-1, sha-256, md5, sha224, sha384, sha512, utf-16 as a string")

        return utf16.hex()
        return hashed_data

    @staticmethod
    def convert_help():
        with open("helpfile", 'w+') as hpo:
            hpo.read()
