import os
print("Hello world!")
print(os.environ.get('PORT'))
print(os.listdir())
print(os.listdir(os.path.join(os.path.abspath("."),'app')))
