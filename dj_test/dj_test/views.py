from django.shortcuts import render
from django.core.cache import cache

def index(request):
#------------------
    ckey="DSnhits465"
    nhits=cache.get(ckey,0)
    nhits+=1
    cache.set(ckey, nhits)
    context={'nhits':nhits}
    return render(request,"index.html",context)

