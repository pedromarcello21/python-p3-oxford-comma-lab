words = ["x","y","z"]

def oxford_comma(items):
    before_oxford = ", ".join(items[:len(items)-1])
    after_oxford = before_oxford + " and " + items[-1]
    return after_oxford


print(oxford_comma(words))
