from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow anyone to read (GET),
    but only authorized/admin users to modify data.
    """
    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user is authenticated and is a staff/admin member
        return request.user and request.user.is_authenticated and request.user.is_staff
