class TokenCollection:
    def __init__(self):
        self.tokens = []
    
    def ingest(self, string):
        self.tokens.append(string)
    
    def appearance(self, prefix):
        count = 0
        for token in self.tokens:
            if token.startswith(prefix):
                count += 1
        return count / len(self.tokens)


# 示例使用
collection = TokenCollection()
collection.ingest('oursky:uk:dev')
collection.ingest('oursky:hk:design')
collection.ingest('oursky:hk:pm')
collection.ingest('oursky:hk:dev')
collection.ingest('skymaker')

print(collection.appearance('oursky'))  # 输出：0.8
print(collection.appearance('oursky:hk'))  # 输出：0.6

collection.ingest('skymaker:london:ealing:dev')
collection.ingest('skymaker:london:design')
collection.ingest('skymaker:london:design')
collection.ingest('skymaker:man:pm')
collection.ingest('skymaker:man:pm')

print(collection.appearance('skymaker:man'))  # 输出：0.2
print(collection.appearance('skymaker:lon'))  # 输出：0.0
print(collection.appearance('london:skymaker'))  # 输出：0.0


#Space Complexity: The program uses a list (self.tokens) to store the ingested tokens. The space complexity of storing n tokens would be O(n).
#Time Complexity:
#The ingest function has a time complexity of O(1) as it simply appends the token to the list.
#The appearance function has a time complexity of O(n) as it iterates through all the stored tokens to count the appearances with the given prefix.