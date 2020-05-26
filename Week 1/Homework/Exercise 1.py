# write your code here!
import string
alphabet=string.ascii_letters
print(alphabet)
print(type(alphabet))
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
# write your code here!
for letter in sentence:
    if letter in alphabet:
        if letter in count_letters:
            count_letters[letter]+=1
        else:
            count_letters[letter]=1
print(count_letters)
# write your code here!
def counter(input_string):  
    count_letters = {}
    for letter in input_string:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter]+=1
            else:
                count_letters[letter]=1
    return count_letters
address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""   

# Write your code here!
address_count=counter(address)
print(address_count)
# write your code here!
most_common_letter=''
max_count=0
for letter, count in address_count.items():
    if count>max_count:
        max_count=count
        most_common_letter=letter
print(most_common_letter)
