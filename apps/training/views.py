from apps.core.generic import build_crud_views
from .models import TrainingRecord

ListView, CreateView, UpdateView, DeleteView = build_crud_views(
    model=TrainingRecord,
    fields=['employee_name', 'course_title', 'provider', 'completed_on', 'expires_on', 'certificate'],
    url_namespace="training",
    page_title="Training Record",
)
