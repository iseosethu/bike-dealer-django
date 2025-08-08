from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class RoleRequiredMixin(AccessMixin):
    """Verify that the current user has the required role."""
    required_role = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if self.required_role and request.user.role != self.required_role:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class AdminRequiredMixin(RoleRequiredMixin):
    required_role = 'A'

class MechanicRequiredMixin(RoleRequiredMixin):
    required_role = 'M'

class CustomerRequiredMixin(RoleRequiredMixin):
    required_role = 'C'