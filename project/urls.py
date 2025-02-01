from rest_framework.routers import DefaultRouter
from .api import vulnerabilityViewSet,vulnerabilityViewSetNoFix,vulnerabilityViewSetseveridad,vulnerabilityViewSetfilter

router = DefaultRouter()
router.register(r'vulnerabilidades',vulnerabilityViewSet, basename="vulnerabilidades")
router.register(r'vulnerabilidades_filtro',vulnerabilityViewSetfilter, basename="vulnerabilidades filtro")
router.register(r'nofixeadas',vulnerabilityViewSetNoFix, basename="vulnerabilidades no fixeadas")
router.register(r'vulnerabilidades_por_severidad',vulnerabilityViewSetseveridad, basename="vulnerabilidades por severidad")
urlpatterns = router.urls