# Walls-That-Talk-First-Steps-in-Federated-Forensics-for-Law-Enforcement-Collaboration

Federated Forensics Architecture Prototype

A research prototype for privacy-preserving, multi-agency digital forensic collaboration using federated learning. The architecture aligns federated learning with law enforcement hierarchies

How to run this code:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
export KAGGLE_API_TOKEN=<YOUR_KAGGLE_API_TOKEN>
make install
make data
make partition SEED=123
make compose
make flower-config
make up
make train GLOBAL_ROUNDS=3 REGIONAL_ROUNDS=2
make eval GLOBAL_ROUNDS=3
make predict GLOBAL_ROUNDS=3
```

Expected outputs:

```text
shared/checkpoints/region_eu/round_<g>.pt
shared/checkpoints/region_na/round_<g>.pt
shared/checkpoints/global/round_<g>.pt
reports/metrics_summary.csv
reports/metrics_summary_global.csv
reports/predictions_lea_eu_01.csv
reports/demo_transcript.txt
```


