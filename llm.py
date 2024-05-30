from gpt4all import GPT4All

model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf", allow_download=False)

output = model.generate("Quel est le sens de la vie ? ", max_tokens=3000)
print(output)
