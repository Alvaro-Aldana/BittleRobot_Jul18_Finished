import variables
from nltk.tokenize import word_tokenize
# using lemmatizing
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()



def test_text(text):
    _list = []
    words = word_tokenize(text)
    for i in range(len(_list)):
        _list.append(lemmatizer.lemmatize(words[i]))
    for x in range(len(_list)):
        print("before:",words[x])
        print("after:",_list[x])
        if _list[x]!=words[x]:
            print(f"ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR        {x}   {words[x]} != {_list[x]}")




#test_list(variables.english_actions)
#test_text("walk forward walk right walk left backward backward left backward right crawl forward crawl right crawl left push forward push right push left run forward run left run right hop spin right spin left handstand wave hand shake one hand pushups pushups lay down butt up stand up come here high five good boy hand up play dead flip over shake head back foot up calibration mode roll over balance bow crouch sit stretch zero stomp angry backflip fight cheer look dig hug jump kick nod pee scratch sniff flat test moonwalk")              

while True:
    test_text(input())





