class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        length = ""
        for word in strs:
            encoded_string += word
            length = "#" + str(len(word)) + length

        return encoded_string + "!" + length

    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        string = ""
        length = ""
        i = 0
        j = len(s) - 1
        while True:
            if s[j] == "#":
                for l in range(int(length)):
                    string += s[l+i]
                decoded_string.append(string)
                i += int(length)
                length = ""
                string = ""
                j -= 1
            if s[j] == '!':
                break
            
            length = s[j] + length
            j -= 1


        return decoded_string
