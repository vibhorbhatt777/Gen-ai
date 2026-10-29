# how are token calculated = using openai token token calculator


# tiktoken - openai official token counter - to see how text is tokenized 
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-5-nano")
tokens = encoding.encode("hi my name is vibhor and i like f1")

# it give token id
print(tokens)
# [3686, 922, 1308, 382, 95463, 9803, 326, 575, 1299, 285, 16]

# now we decode the token_id that we print the above

for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id} = {token_text}")

# final output
# [3686, 922, 1308, 382, 95463, 9803, 326, 575, 1299, 285, 16]
# 3686 = hi
# 922 =  my
# 1308 =  name
# 382 =  is
# 95463 =  vib
# 9803 = hor
# 326 =  and
# 575 =  i
# 1299 =  like
# 285 =  f
# 16 = 1

# A token is a small unit of text (a word or part of a word). Every prompt and response uses tokens, which affects:
# Cost: You pay per token used
# Speed: Fewer tokens = faster response
# Quality: Sometimes shorter responses are better, sometimes you need more detail