from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsTaskAuthorOrReadOnly


class TodoList(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('is_complete', 'set_to_complete', 'goal_set_date')




class TodoRetrieve(RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    lookup_field = 'id'



class TodoUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated, IsTaskAuthorOrReadOnly]
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


