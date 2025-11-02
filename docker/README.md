# Dockerfiles for srsRAN and Monitoring Components

This directory contains all Dockerfiles used to build the images for the srsRAN-based 5G deployment and monitoring setup.

Each image can be built manually or automatically through the GitHub Actions workflow defined in `.github/workflows/docker-builder.yml`.

---

## 🧱 Images Overview

| Image | Description | Dockerfile |
|--------|--------------|-------------|
| `srsran-gnb-zmq` | gNB using ZMQ interface (for simulation) | [`Dockerfile.gNB.zmq`](./Dockerfile.gNB.zmq) |
| `srsran-gnb-uhd` | gNB with UHD (USRP) backend | [`Dockerfile.gNB.uhd`](./Dockerfile.gNB.uhd) |
| `srsran-gnb-dpdk` | High-performance gNB using DPDK | [`Dockerfile.gNB.dpdk`](./Dockerfile.gNB.dpdk) |
| `srsue` | UE with ZMQ interface | [`Dockerfile.srsUE`](./Dockerfile.srsUE) |
| `telegraf` | Telegraf agent to collect and export metrics | [`Dockerfile.telegraf`](./Dockerfile.telegraf) |

---