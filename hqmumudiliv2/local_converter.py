from hqmumudiliv2 import encrypt, decrypt
print("program started. (using lib hqmumudiliv2)")
while True:
    mode = input("choose mode: E/D (C for exit)").upper()
    if mode == "E":
        try:
            input_to_convert = input("to encrypt: ")
            print(encrypt(input_to_convert))
        except KeyError as e:
            print(f"an error occured while encrypting: key {e} is not in the encypting keyboard. You cant encrypt this symbol.")
    elif mode == "D":
        try:
            input_to_convert = input("to decrypt: ")
            print(decrypt(input_to_convert))
        except KeyError:
            print("This is an invalid encrypted value. This value doesnt match properly with the decrypting technique.")
    elif mode == "C":
        break
    else:
        print("invalid mode")
print("program closed.")