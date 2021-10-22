from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoListItem 
from django.http import HttpResponseRedirect , HttpResponse
from .serializers import UserSerializer

# Create your views here.
class index(APIView):
    def get(self,request,format=None):
        all_todo_items = TodoListItem.objects.all()
        serializer = UserSerializer( all_todo_items  , many=True)
        return  Response(serializer.data)
    
    def post(self,request):
        '''x = request.POST['content']
        new_item = TodoListItem(content = x)
        new_item.save()
        return HttpResponseRedirect('/')'''
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.get(request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
    def delete(self,request):
        '''y = TodoListItem.objects.get(id= i)
        y.delete()
        return HttpResponseRedirect('/')''' 
        if not (isinstance(request.data['id'], list)):user = TodoListItem.objects.filter(id=request.data['id'])
        else : user = TodoListItem.objects.all()
        user.delete()
        return self.get(request)
    
