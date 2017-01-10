from rest_framework.permissions import BasePermission
from parkstay.helpers import is_officer, is_customer


# REST permissions
class OfficerPermission(BasePermission):
    def has_permission(self, request, view):
        return is_officer(request.user)