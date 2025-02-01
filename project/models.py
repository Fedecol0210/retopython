from django.db import models


class Vulnerabilidad(models.Model):
    cve_id = models.CharField(max_length=50, unique=True)  # ID CVE único
    source_identifier = models.CharField(max_length=200, null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    vuln_status = models.CharField(max_length=50, null=True, blank=True)
    Bseverity = models.CharField(max_length=20, choices=[
        ('HIGHT', 'HIGHT'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    ], null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True, choices=[
        ('OPEN', 'OPEN'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('FIXED', 'FIXED'),
        ('REJECTED', 'REJECTED'),
])
   
  
