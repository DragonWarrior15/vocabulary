import random
# from itertools import permutations

def generate_permutation(list_object):
    return_list = []
    while len(list_object) > 0:
        random_index = random.randint(0, len(list_object) - 1)
        return_list.append(list_object[random_index])
        list_object.pop(random_index)
    return (return_list)

# eng_file = 'english_words_easy.csv'
eng_file = 'english_words_revise.csv'
# eng_file = 'english_words_medium.csv'

f = open(eng_file)
words = f.read()
f.close()

words = words.split('\n')
words = [word.split(',') + [1, 1] for word in words]

while(1):
    # display the question
    # random_index = random.randint(0, len(words))
    # random_index = random.randint(0, 45)
    random_permutation = generate_permutation(list(range(0, len(words))))
    # print (random_permutation)
    for random_index in random_permutation:
        words[random_index][3] += 1
        input_ans = raw_input('Meaning of ' + str(words[random_index][0]) + ' ' + str(words[random_index][2] - 1) + '/' + str(words[random_index][3] - 2) + ' is : ')
        if input_ans == words[random_index][1]:
            print ('Correct ans')
            words[random_index][2] += 1
        else:
            print ('Incorrect, the meaning is : ' + str(words[random_index][1]))
