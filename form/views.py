from django.shortcuts import render
from django.http import HttpResponse
from form.models import Info

# Create your views here.

def home(request):
    return render(request, 'home.html')


def form(request):
    print("DATA=", request.POST)

    # to save data imported from browser
    if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        un = request.POST["uname"]
        ad = request.POST["addRe"]
        ci = request.POST["cityn"]
        st = request.POST["state"]
        pi = request.POST["pinco"]
        # ch = request.POST["check"]
        # return HttpResponse("<h1>"+fn+ln+em+un+ad+st+pi+"</h1>")
        data = Info(
            fname = fn,
            lname = ln,
            email = em,
            uname = un,
            addRe = ad,
            cityn = ci,
            state = st,
            pinco = pi,
        )
        data.save()
        print(data)
        # return HttpResponse("Data saved in table successfully")
    return render(request, 'form.html')

