from itertools import count

from django.contrib import messages
from django.shortcuts import render, redirect
from.models import *
from .forms import *
# Create your views here.

def add(request):
        if request.method == "POST":
            a = studentform(request.POST)
            if a.is_valid():
                nm = a.cleaned_data['sname']
                dob = a.cleaned_data['dob']
                phy = a.cleaned_data['phy']
                chem = a.cleaned_data['chem']
                maths = a.cleaned_data['maths']
                cs = a.cleaned_data['cs']
                marks=[phy,chem,maths,cs]
                for i in marks:

                    if i<0 or i>100:
                        messages.info(request, "Marks must between 0-100")
                        return redirect(add)

                else:
                    total = sum(marks)
                    per = (total / 400) * 100

                    b = student(sname=nm, dob=dob, phy=phy, chem=chem, maths=maths, cs=cs, per=per)
                    b.save()
                    return redirect(view)

            else:
                messages.info(request,'Please fill out the fields')
                return redirect(add)
        else:
            return render(request,'adddetails.html')


def view(request):
    a = student.objects.all()

    name = []
    dob = []
    phy = []
    chem = []
    maths=[]
    cs=[]
    per=[]
    for i in a:

        nm = i.sname
        name.append(nm)
        dob1 = i.dob
        dob.append(dob1)
        phys = i.phy
        phy.append(phys)
        chemm = i.chem
        chem.append(chemm)
        math = i.maths
        maths.append(math)
        css = i.cs
        cs.append(css)
        perc=i.per
        per.append(perc)
    mylist = zip(name, dob, phy, chem, maths,cs,per)
    return render(request, 'display.html', {'mylist': mylist})


