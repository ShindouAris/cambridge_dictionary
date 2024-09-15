# cambridge_dictionary


- USAGE:
```python
from cambridge_dictionary import Cambridge_Dictionary
from cambridge_dictionary.error import ApiError, NotFoundWord
from asyncio import run

async def check_word(word: str):
    dictionary = Cambridge_Dictionary()
    return await dictionary.dictionary_check(word)

if __name__ == '__main__':
    while True:
        user_input = input("> ")
        try: 
            print(run(check_word(user_input)))
        except NotFoundWord as e:
            print(e)
        except ApiError as e:
            print(e)
```
