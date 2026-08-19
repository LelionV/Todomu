from apps.core.generic import build_crud_views
from .models import RiskAssessment

ListView, CreateView, UpdateView, DeleteView = build_crud_views(
    model=RiskAssessment,
    fields=['site', 'activity', 'hazards_identified', 'existing_controls', 'likelihood', 'severity', 'status', 'review_date'],
    url_namespace="risk",
    page_title="Risk Assessment",
)
