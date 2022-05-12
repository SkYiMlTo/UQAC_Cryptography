import math


class DES:
    def __init__(self):
        self.__s1 = [["101", "010", "001", "110", "011", "100", "111", "000"], ["011", "100", "110", "010", "000", "111", "101", "011"]]
        self.__s2 = [["100", "000", "110", "101", "111", "001", "011", "010"], ["101", "011", "000", "111", "110", "010", "001", "100"]]

    def trois_encryptions(self, message_clair, keyK):
        MULTIKEY = isinstance(keyK, list) and len(keyK) == 3
        binary_msg = self.__toBinary(message_clair)
        output = []
        # result = message_clair
        for character in binary_msg:
            result = character
            # character = character[1:]
            for i in range(3):
                Lminus1 = result[:len(result) // 2]
                Rminus1 = result[len(result) // 2:]
                if MULTIKEY:
                    result = self.__encryption(Lminus1, Rminus1, keyK[i])
                else:
                    result = self.__encryption(Lminus1, Rminus1, keyK)
                # print(f"Message crypté {i+1} fois: {result}")  # Testing / Debug
            output.append(result)
        return self.__toString(output)

    def __encryption(self, Lminus1, Rminus1, keyK):
        f_nk = self.__calc_f_rk(Rminus1, keyK)
        R = bin(int(f_nk, 2) ^ int(Lminus1, 2)).split('b')[1]
        return Rminus1.zfill(6) + R.zfill(6)

    def trois_decryptions(self, message_chiffre, keyK):
        MULTIKEY = isinstance(keyK, list) and len(keyK) == 3
        binary_msg = self.__toBinary(message_chiffre)
        output = []
        # result = message_chiffre
        for character in binary_msg:
            result = character
            for i in range(3):
                L = result[:len(result) // 2]
                R = result[len(result) // 2:]
                if MULTIKEY:
                    result = self.__decryption(L, R, keyK[2 - i])
                else:
                    result = self.__decryption(L, R, keyK)
                # print(f"Message décrypté {i+1} fois: {result}")  # Testing / Debug
            output.append(result)
        return self.__toString(output)

    def __decryption(self, L, R, K):
        f_nk = self.__calc_f_rk(L, K)
        Lminus1 = bin(int(f_nk, 2) ^ int(R, 2)).split('b')[1]
        return Lminus1.zfill(6) + L.zfill(6)

    def __calc_f_rk(self, Rminus1, keyK):
        Rminus1expanded = self.__expansion(Rminus1)  # 6 to 8 bits
        outputXOR = bin(int(Rminus1expanded, 2) ^ int(keyK, 2)).split('b')[1].zfill(8)  # XOR Ri-1 and K

        part1 = outputXOR[:len(outputXOR)//2]  # Get the two parts of the message
        part2 = outputXOR[len(outputXOR)//2:]

        firstPart = self.__s1[int(part1[:1])][int(part1[1:], 2)]  # Using the sboxs
        secondPart = self.__s2[int(part2[:1])][int(part2[1:], 2)]

        return firstPart + secondPart

    def __expansion(self, mess_to_expand):
        myArray = list(mess_to_expand)
        myArray.insert(4, myArray[2])
        myArray.insert(2, myArray[3])
        return "".join(myArray)

    def __toBinary(self, a):
        l, m = [], []
        l.extend(ord(i) for i in a)
        m.extend(str(bin(i)[2:]) for i in l)
        for i in range(len(m)):
            m[i] = m[i].zfill(12)
        return m

    def __toString(self, a):
        l = []
        m = ""
        for i in a:
            i = int(i)
            b = 0
            c = 0
            k = int(math.log10(i)) + 1
            for j in range(k):
                b = ((i % 10) * (2 ** j))
                i = i // 10
                c = c + b
            l.append(c)
        for x in l:
            m = m + chr(x)
        return m