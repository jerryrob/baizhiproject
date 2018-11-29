from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.paginator import Paginator
import json
import json,re
from crawerapp.models import Films
# Create your views here.
def saveFilms(request):
    with open(r"D:\project\emc\crawerapp\films.txt", 'r', encoding="utf-8") as f:
        s = f.readlines()
        for i in s:
            film = json.loads(i)
            pattern = re.compile('movie/(.*?)@', re.S)
            items = re.findall(pattern, film["image"])
            img = "img/films/" + items[0].strip()

            Films.objects.create(title=film["title"], actor=film["actor"], time=film["time"], image=img,
                                 score=float(film["score"]), index=film["index"]).save()
def queryPage(request):

    # 要查询第num页（从1开始）
    num = request.GET.get("num")
    if not num:
        num = 1
    size = 10
    # 当前页的对象
    page = Paginator(Films.objects.all(), size).page(num)
    return render(request, "crawer/top.html",{"page":page})
