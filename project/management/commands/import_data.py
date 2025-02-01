
import requests
from django.core.management.base import BaseCommand
from project.models import Vulnerabilidad

class Command (BaseCommand):
    help='consumir bd'

    def handle(self, *args, **options):
        url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
        params = {
            'resultsPerPage': '6',
            'startIndex': '0'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Respuesta de la API exitosa. Datos recibidos:")
            data = response.json()
            print("Datos recibidos:", data)
            vulnera = data.get('vulnerabilities', [])
            if not vulnera:
                print("No se encontraron vulnerabilidades en la respuesta.")
            for vuln in vulnera:
                cve_data = vuln.get('cve', {})
                cve_id = cve_data.get('id', '')
                source_identifier = cve_data.get('sourceIdentifier', '')
                published = cve_data.get('published', '')
                last_modified = cve_data.get('lastModified', '')
                metrics = cve_data.get('metrics', {})
                cvss_metric_v2 = metrics.get('cvssMetricV2', [])
                base_severity = None
                if cvss_metric_v2:
                    base_severity = cvss_metric_v2[0].get('baseSeverity', '')
                vuln_status = cve_data.get('vulnStatus', '')

                vulnerabilidad = Vulnerabilidad(
                    cve_id=cve_id,
                    source_identifier=source_identifier,
                    published=published,
                    last_modified=last_modified,
                    Bseverity=base_severity,
                    vuln_status=vuln_status
                )
                vulnerabilidad.save()
                

            
        else:
             self.stdout.write(self.style.ERROR(f"Error al obtener datos de la API: {response.status_code}"))