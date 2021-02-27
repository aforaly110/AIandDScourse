from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    val1 = request.GET.get('num1')
    val2 = request.GET.get('num2')
    op = request.GET.get("op")
    ans = None
    if op == "+":
        ans = int(val1) + int(val2)

    elif op == "-":
        ans = int(val1) - int(val2)

    elif op == "*":
        ans = int(val1) * int(val2)

    elif op == "/":
        ans = int(val1) / int(val2)

    else:
        ans = "something went wrong"

    result = {"ans" : ans}
    
    return render(request, "about.html" , result)

def contact(request):
    return render(request, "contact.html")