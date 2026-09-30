import time
import uuid
from datetime import datetime, timezone

# Génère une chaîne aléatoire unique au démarrage
random_string = str(uuid.uuid4())

# Boucle infinie qui s'exécute toutes les 5 secondes
while True:
    # Horodatage au format ISO UTC (ex: 2026-09-30T07:10:00.000Z)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    
    # flush=True est crucial en Docker pour voir les logs immédiatement dans terminal / kubectl logs
    print(f"{timestamp}: {random_string}", flush=True)
    
    time.sleep(5)