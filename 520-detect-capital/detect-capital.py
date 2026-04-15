class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s=len(word)
        cu=0
        cl=0
        for i in word:
            if i.isupper():
                cu+=1
            if i.islower():
                cl+=1

        if cu==s or cl==s or (word[0].isupper() and word[1:].islower()):
            return True
        return False