from rest_framework import permissions

from users.models import User

class CRUDPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        pass