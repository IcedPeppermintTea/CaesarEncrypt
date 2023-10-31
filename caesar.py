"""
Caesar Cypher Encryption Crack
"""
from string import printable # get the alphabet

if __name__ == "__main__":
    phrase = "vjg1fqi1twpu:"
    key = 1
    mode = "d" # encrypt or decrypt
    codex = printable.strip()
    codex += " " # add in spaces

    transformed = ""

    for i in range(len(codex)):  # print out every possible combination (since we do not know the key)
        key += 1  # increment the key for however many characters we have (26)
        for token in phrase:
            if token in codex:
                tokenidx = codex.find(token)
                # print(token)
                # print(tokenidx)
                if mode == "e":
                    transformidx = (tokenidx + key) % len(codex)
                else:
                    transformidx = (tokenidx - key) % len(codex)

                transformed += codex[transformidx]

            else:
                transformed += token

    print(transformed)

