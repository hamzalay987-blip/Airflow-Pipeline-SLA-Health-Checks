import csv
from collections import defaultdict
from datetime import datetime

def run(path='data/dag_runs.csv'):
    groups=defaultdict(list)
    with open(path,newline='') as f:
        for row in csv.DictReader(f): groups[row['dag_id']].append(row)
    breaches={}
    for dag,rows in groups.items():
        errors=sum(r['status']!='success' for r in rows)
        slow=sum(int(r['duration_seconds'])>int(r['sla_seconds']) for r in rows)
        causes=[]
        if errors: causes.append('run_failures')
        if slow: causes.append('slow_runs')
        if causes: breaches[dag]=causes
    return {'dags_checked':len(groups),'unhealthy_dags':breaches}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
