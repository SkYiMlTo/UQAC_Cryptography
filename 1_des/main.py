from des import DES


def main():
    myDES = DES()

    MESSAGE = "Bonjour, ceci est un test !"
    KEY = "01100101"

    encrypted_message = myDES.trois_encryptions(MESSAGE, KEY)
    decrypted_message = myDES.trois_decryptions(encrypted_message, KEY)

    print(f"Encryption avec une seule clé : {KEY}")
    print(f"Message original : {MESSAGE}")
    print(f"Message crypté : {encrypted_message}")
    print(f"Message décrypté : {decrypted_message}")
    print("----------")

    MESSAGE = "Message encrypté avec plusieurs clés !"
    KEYS = ["01000001", "01100101", "01001101"]

    encrypted_message = myDES.trois_encryptions(MESSAGE, KEYS)
    decrypted_message = myDES.trois_decryptions(encrypted_message, KEYS)

    print(f"Encryption avec plusieurs clés : {KEYS}")
    print(f"Message original : {MESSAGE}")
    print(f"Message crypté : {encrypted_message}")
    print(f"Message décrypté : {decrypted_message}")

if __name__ == '__main__':
    main()

# DRAFT

# MESSAGE = "011100100110"
# MESSAGE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# MESSAGE = "abcdefghilklmnopqrstuvwxyz"
# encrypted_message = myDES.encryption("011100", "100110", KEY)
# decrypted_message = myDES.decryption("100110", "011000", KEY)
