from django.shortcuts import render
from django.core.cache import cache
import logging

def index(request):
#------------------
    nhits=0
    try:
        ckey="DSnhits465"
        nhits=cache.get(ckey,0)
        nhits+=1
        cache.set(ckey, nhits)
    except Exception as e:
        logging.warning(f"Exception : {str(e)}")
    context={'nhits':nhits}
    return render(request,"index.html",context)

