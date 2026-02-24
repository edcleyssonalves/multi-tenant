from django.core.exceptions import PermissionDenied



class UserIsOwnerMixin:

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.user != self.request.user:
            raise PermissionDenied
        return  super().dispatch(request, *args, **kwargs)