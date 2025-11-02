# Helm Charts for srsRAN and Telegraf

This directory contains Helm charts for deploying the **srsRAN gNB**, **srsRAN UE**, and **Telegraf** monitoring components.

These charts are intended for use with:
- [Open5GS Core Network](https://github.com/yassir63/open5gs-k8s)
- [5G Monarch Monitoring Framework](https://github.com/Ziyad-Mabrouk/5g-monarch)

---

## 📘 Available Charts

| Chart | Description |
|--------|--------------|
| [`srsran-gnb`](./srsran-gnb) | Deploys the srsRAN gNB with ZMQ, UHD, or DPDK support |
| [`srsran-ue`](./srsran-ue) | Deploys one or multiple simulated UEs |
| [`telegraf`](./telegraf) | Deploys Telegraf for metrics collection and export |

---

## 🚀 Usage

### 1️⃣ Deploy gNB

Default (ZMQ mode):
```bash
helm install srsran-gnb ./srsran-gnb -n open5gs
```

Other configurations:

```bash
helm install srsran-gnb ./srsran-gnb -f values-n300.yaml -n open5gs
```
```bash
helm install srsran-gnb ./srsran-gnb -f values-n320.yaml -n open5gs
```

### 2️⃣ Deploy UE

```bash
helm install srsran-ue ./srsran-ue -n open5gs
```

### 3️⃣ Deploy Telegraf for Monitoring

```bash
helm install telegraf ./telegraf -n open5gs
```