from django.test import TestCase
import pickle,unittest,json,re

from crawerapp.models import  Films
class NamesTestCade(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):

        with open("films.txt", 'r', encoding="utf-8") as f:
            s=f.readlines()
            for i in s:
                film=json.loads(i)

                pattern = re.compile('movie/(.*?)@', re.S)
                items = re.findall(pattern, film["image"])
                img="img/films/"+items[0].strip()

                Films.objects.create(title=film["title"],actor=film["actor"],time=film["time"],image=img,score=float(film["score"]),index=film["index"]).save()


unittest.main(NamesTestCade())
