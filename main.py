def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        file_contents = f.read()

#it's word's amount in the book:
    words_num = len(file_contents.split()) 
    #print(words_num)
    
    answer = {}

# it's counting unique characters and make a dic in "char":"amount" pair:
    for i in range(0, len(file_contents)): 
        character = file_contents[i].lower()
        if character not in answer:
            answer[character] = 1
        else:
            answer[character] += 1

# it's counting unique letters and make a dic in "letter":"amount" pair:
    letter_dic = {}
    for i in range(0, len(file_contents)): 
        character = file_contents[i].lower()
        if character not in letter_dic and character.isalpha():
            letter_dic[character] = 1
        elif character in letter_dic and character.isalpha():
            letter_dic[character] += 1
    #print(letter_dic)

# it's converting for sorting
    newest = []
    for n in letter_dic:
        newest.append({"char":n, "num":letter_dic[n]})
    #print(newest)

    def sort_on(dict):
        return dict["num"]
    
    newest.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_num} words found in the document\n")
    for n in newest:
        log_message = f"The '{n['char']}' character was found {n['num']} times"
        print(log_message)
    print("--- End report ---")

main()