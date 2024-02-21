from rest_framework.permissions import BasePermission

class IsAdminOrAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Checking if the user is an admin
        if request.user.is_staff:
            return True
        # Checking if the user is the author
        return obj.author == request.user