import aiohttp
import fake_useragent
from .error import (NotFoundWord, ApiError)


def gen_user_agents() -> str:
    return f"{fake_useragent.UserAgent.chrome}"

class Cambridge_Dictionary:
    def __init__(self):
        self.origin_url = "https://dictionary.cambridge.org/dictionary/english/"

    async def dictionary_check(self, word):

        headers = {'User-Agent': gen_user_agents()}
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"https://dictionary.cambridge.org/dictionary/english/{word}", headers=headers)

        if response.ok:

            if str(response.url) == self.origin_url:
                raise NotFoundWord(word)

            return f"Đã tìm thấy từ: {word} {response.url}"

        else:
            raise ApiError(response.status)
