import zmq
import threading
import os
import json

GNB_DL_PORT = int(os.environ["GNB_DL_PORT"])
GNB_UL_PORT = int(os.environ["GNB_UL_PORT"])
UES = json.loads(os.environ["UES_CONFIG"])

context = zmq.Context()

# Reçoit DL du gNB (gNB fait PUSH, broker fait PULL)
gnb_rx = context.socket(zmq.PULL)
gnb_rx.bind(f"tcp://0.0.0.0:{GNB_DL_PORT}")

# Renvoie UL au gNB (broker fait PUSH, gNB fait PULL)
gnb_tx = context.socket(zmq.PUSH)
gnb_tx.bind(f"tcp://0.0.0.0:{GNB_UL_PORT}")

ue_tx_sockets = []
ue_rx_sockets = []

for ue in UES:
    # DL vers UE (broker PUSH → UE PULL)
    s_tx = context.socket(zmq.PUSH)
    s_tx.connect(f"tcp://{ue['ip']}:{ue['dl_port']}")
    ue_tx_sockets.append(s_tx)
    # UL depuis UE (UE PUSH → broker PULL)
    s_rx = context.socket(zmq.PULL)
    s_rx.bind(f"tcp://0.0.0.0:{ue['ul_port']}")
    ue_rx_sockets.append(s_rx)

def downlink():
    while True:
        msg = gnb_rx.recv()
        for s in ue_tx_sockets:
            s.send(msg, copy=False)

def uplink(idx):
    s = ue_rx_sockets[idx]
    while True:
        msg = s.recv()
        gnb_tx.send(msg, copy=False)

threading.Thread(target=downlink, daemon=True).start()
for i in range(len(UES)):
    threading.Thread(target=uplink, args=(i,), daemon=True).start()

print(f"Broker running — GNB_DL:{GNB_DL_PORT} GNB_UL:{GNB_UL_PORT} UEs:{UES}", flush=True)
threading.Event().wait()
