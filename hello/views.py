from django.http import HttpResponse

def index(request):
    response = ""
    for i in range(1, 4):  # i는 몇 번째 세트인지를 나타냄
        response += "회원님~! {} 세트 시작하겠습니다\n".format(i)
        for j in range(1, 11):  # j는 해당 세트에서 동작을 몇 번 반복했는지를 나타냄
            response += "{}\n".format(j)
    return HttpResponse(response)