import pandas as pd
from django.shortcuts import render

from .models import Student


# Create your views here.
def home(request):
    item = Student.objects.all().values()
    df = pd.DataFrame(item)
    df1 = df.name.tolist()
    df = df['rank'].tolist()
    mydict = {
        'df': df,
        'df1': df1,
    }
    return render(request, 'charts/index.html', context=mydict)
