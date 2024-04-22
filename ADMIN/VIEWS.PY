from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

class UserListCreateView(generics.ListCreateAPIView):
    # Previous code...

    permission_classes = [IsAdminUser]  # Only admin can create or list users

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Previous code...

    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users can retrieve, update, or delete their own user data