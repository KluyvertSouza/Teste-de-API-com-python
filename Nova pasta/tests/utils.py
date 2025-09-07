import time
import requests

def request_with_retry(url, method='GET', headers=None, payload=None, retries=3, delay=2):
    """
    Executa requisição HTTP com retry em caso de falhas temporárias.
    """
    for attempt in range(1, retries + 1):
        try:
            response = requests.request(method, url, headers=headers, json=payload, timeout=5)
            response.raise_for_status()
            return response
        except Exception as e:
            if attempt == retries:
                raise
            time.sleep(delay)
