# srsran-gnb Helm Chart

Helm chart for deploying the srsRAN gNB with ZMQ, UHD and DPDK support. 

## Usage

Default ZMQ deployment:
```bash
helm install srsran-gnb ./ -n open5gs -f values-rfsim.yaml
```

For other configurations, use `-f` with one of the following files:

```bash
helm install srsran-gnb ./ -n open5gs -f <values-n300.yaml | values-n320.yaml>
```

> **NOTE:** _Benetel_ and _Liteon_ values are just placeholders for now and not ready for use.