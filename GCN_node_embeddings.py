import pandas as pd
import networkx as nx
import torch
from torch_geometric.data import Data
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
import openpyxl


node_features_df = pd.read_csv('D:/fengzhen/MFEPre/Struct2Graph/3IAB_A_centrality.txt', delimiter='\t', header=None)
node_features = torch.tensor(node_features_df.iloc[:, 1:].values, dtype=torch.float)


edges_df = pd.read_csv('D:/fengzhen/MFEPre/Struct2Graph/3IAB_A_edgelist.txt', delimiter='\t', header=None)

node_to_idx = {node: idx for idx, node in enumerate(node_features_df.iloc[:, 0])}
# 构建边的tensor
edge_list = [[node_to_idx[src], node_to_idx[dst]] for src, dst in edges_df.values]
edge_index = torch.tensor(edge_list, dtype=torch.long).t().contiguous()


data = Data(x=node_features, edge_index=edge_index)

class GCN(torch.nn.Module):
    def __init__(self, num_features, num_classes):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(num_features, 16)
        self.conv2 = GCNConv(16, num_classes)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = self.conv2(x, edge_index)
        return x


model = GCN(num_features=node_features.shape[1], num_classes=1024)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)


model.train()
for epoch in range(500):
    optimizer.zero_grad()
    out = model(data)
    loss = F.mse_loss(out, torch.randn_like(out))
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

model.eval()
with torch.no_grad():
    node_embeddings = model(data)
    df = pd.DataFrame(node_embeddings)


    df.to_excel("D:/fengzhen/MFEPre/Struct2Graph/3IAB_A_node_embeddings.xlsx", index=False)