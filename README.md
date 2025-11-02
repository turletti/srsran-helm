# Helm Charts for srsRAN

This repository provides **Helm charts** and **Dockerfiles** to deploy and build the [`srsRAN`](https://github.com/srsran/srsRAN_Project) 5G components, including gNBs, UEs, and Telegraf-based monitoring agents, on a Kubernetes cluster.

The setup is designed to interoperate with:
- The [Open5GS Core Network](https://github.com/yassir63/open5gs-k8s)
- The [5G Monarch Monitoring Framework](https://github.com/Ziyad-Mabrouk/5g-monarch)

---

## 📦 Repository Structure

```
srsran-helm/
├── charts/                      # Helm charts for gNB, UE, and Telegraf
│   ├── srsran-gnb/
│   ├── srsran-ue/
│   └── telegraf/
├── docker/                      # Dockerfiles for all components
│   ├── Dockerfile.gNB.zmq
│   ├── Dockerfile.gNB.uhd
│   ├── Dockerfile.gNB.dpdk
│   ├── Dockerfile.srsUE
│   └── Dockerfile.telegraf
│   ├── resources/              # Config files used for building Telegraf agent image compatible with srsRAN monitoring
└── .github/workflows/docker-builder.yml   # Automated GHCR image build pipeline
```

## 🧩 Components

| Component         | Description                           | Image Tag | Helm Chart          |
|-------------------|---------------------------------------|------------|---------------------|
| srsran-gnb-zmq    | gNB with ZMQ front-end                 | v1.0       | [charts/srsran-gnb](./charts/srsran-gnb/)   |
| srsran-gnb-uhd    | gNB using UHD (USRP) driver            | v1.0       | [charts/srsran-gnb](./charts/srsran-gnb/)   |
| srsran-gnb-dpdk   | High-performance DPDK-based gNB        | v1.0       | [charts/srsran-gnb](./charts/srsran-gnb/)   |
| srsue             | Simulated UE using ZMQ                 | v1.0       | [charts/srsue](./charts/srsue/)    |
| telegraf          | Metrics collector for gNB monitoring   | v1.0       | [charts/telegraf](./charts/telegraf/)     |

## 🚀 Deployment Overview

### 1️⃣ Build or Pull Images

You can either use the pre-built GHCR images or build them locally:

```bash
docker build -t ghcr.io/ziyad-mabrouk/srsran-gnb-zmq:v1.0 -f docker/Dockerfile.gNB.zmq docker/
```

### 2️⃣ Deploy Open5GS Core

Deploy the Open5GS core following: https://github.com/yassir63/open5gs-k8s 

### 3️⃣ Deploy the gNB, UE, and Telegraf

Use Helm:

```bash
helm install srsran-gnb charts/srsran-gnb/
```
```bash
helm install srsran-ue charts/srsran-ue/
```
```bash
helm install telegraf charts/telegraf/
```

### 4️⃣ Enable Monitoring

Metrics are exported via Telegraf and visualized through the [5G Monarch monitoring stack](https://github.com/Ziyad-Mabrouk/5g-monarch).

