class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for s in strs:
            lStr = len(s)
            encodedStr += str(lStr) + "#" + s
        return encodedStr

    def decode(self, encodedStr : str) -> List[str]:
        decodeStr, i = [], 0

        while i < len(encodedStr):
            j = i
            while encodedStr[j] != "#":
                j += 1
            length = int(encodedStr[i:j])
            decodeStr.append(encodedStr[j+1 : j+1 + length])
            i = j+1+length
        return decodeStr
