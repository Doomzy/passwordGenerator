from django.shortcuts import render, redirect
import string, random

def generator(request):
    return render(request, 'generatorPage.html')

def password(request):
    if request.method == 'POST':
        characters=[]
        length= request.POST.get('passLength')
        if request.POST.get('upperChar'): 
            characters.extend(list(string.ascii_uppercase))
        if request.POST.get('lowerChar'): 
            characters.extend(list(string.ascii_lowercase))
        if request.POST.get('digits'): 
            characters.extend(list(string.digits))
        generatedPass= ''.join(random.choices(
            characters,
            k= int(length)))
        return render(request, 'password.html', {'password': generatedPass})
    return render(request, 'password.html')