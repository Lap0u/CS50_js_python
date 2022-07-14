from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def notfound(request):
    return render(request, "encyclopedia/notfound.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entries = util.list_entries()
    if entry in entries:
        
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(util.get_entry(entry)),
            "entryname": entry
        })
    else :
        return notfound(request)

def research(request):
    
